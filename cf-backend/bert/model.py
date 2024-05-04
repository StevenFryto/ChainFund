import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from transformers import BertModel, BertTokenizer, BertConfig
import numpy as np
import random
import os 
import sys

torch.manual_seed(0)
np.random.seed(0)
random.seed(0)

model_path = '.\\cf-backend\\bert\\checkpoints\\bert'
tokenizer = BertTokenizer.from_pretrained(model_path)
bert_model = BertModel.from_pretrained(model_path)

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(MultiHeadAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads
        assert self.head_dim * heads == embed_size, "Embed size needs to be divisible by heads"
        
        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False)
        self.fc_out = nn.Linear(heads * self.head_dim, embed_size)

    def forward(self, values, keys, queries):
        N = queries.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], queries.shape[1]

        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.heads, self.head_dim)
        queries = queries.reshape(N, query_len, self.heads, self.head_dim)

        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
        attention = torch.softmax(energy / (self.embed_size ** (1 / 2)), dim=-1)

        out = torch.einsum("nhql,nlhd->nqhd", [attention, values])
        out = out.reshape(N, query_len, self.heads * self.head_dim)
        return self.fc_out(out)

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(MultiHeadAttention, self).__init__()
        self.embed_size = embed_size  # : 768
        self.heads = heads            # : 4
        self.head_dim = embed_size // heads  # 768 // 4 = 192
        
        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)  # [192 -> 192]
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)    # [192 -> 192]
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False) # [192 -> 192]
        self.fc_out = nn.Linear(heads * self.head_dim, embed_size)         # [768 -> 768]

    def forward(self, values, keys, queries):
        N = queries.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], queries.shape[1]

        # [N, value_len, embed_size] -> [N, value_len, heads, head_dim]
        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.heads, self.head_dim)
        queries = queries.reshape(N, query_len, self.heads, self.head_dim)

        # energy: [N, heads, query_len, key_len]
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
        # attention: [N, heads, query_len, key_len]
        attention = torch.softmax(energy / (self.embed_size ** (1 / 2)), dim=3)
        # out: [N, query_len, heads, head_dim]
        out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(N, query_len, self.heads * self.head_dim)
        # 最终结果: [N, query_len, embed_size]
        return self.fc_out(out)

class ContrastiveAndPredictiveModel(nn.Module):
    def __init__(self, num_users, embedding_size):
        super(ContrastiveAndPredictiveModel, self).__init__()
        self.user_embedding = nn.Embedding(num_embeddings=num_users, embedding_dim=embedding_size)
        self.publisher_embedding = nn.Embedding(num_embeddings=num_users, embedding_dim=embedding_size)
        self.bert_model = bert_model
        self.attention = MultiHeadAttention(768, heads=4)
        self.fc_info = nn.Linear(768, 128)
        self.fc_user_prediction = nn.Linear(128 + embedding_size, num_users)
        self.fc_duration = nn.Linear(128 + 2 * embedding_size, 1)

    def forward(self, user_ids, publisher_id, pos_texts, neg_texts):
        user_vec = self.user_embedding(user_ids)
        publisher_vec = self.publisher_embedding(publisher_id)
        
        pos_embedded = self.bert_model(**tokenizer(pos_texts, return_tensors='pt', padding=True, truncation=True, max_length=512))['last_hidden_state']
        neg_embedded = self.bert_model(**tokenizer(neg_texts, return_tensors='pt', padding=True, truncation=True, max_length=512))['last_hidden_state']
        
        pos_features = self.attention(pos_embedded, pos_embedded, pos_embedded)
        neg_features = self.attention(neg_embedded, neg_embedded, neg_embedded)

        pos_features = pos_features.mean(dim=1)  # 减少到 [batch_size, 768]
        neg_features = neg_features.mean(dim=1)  # 减少到 [batch_size, 768]

        pos_features = F.leaky_relu(self.fc_info(pos_features))
        neg_features = F.leaky_relu(self.fc_info(neg_features))

        duration_input = torch.cat((pos_features, user_vec, publisher_vec), dim=1)
        duration_output = self.fc_duration(duration_input)
        user_prediction_input = torch.cat((pos_features, publisher_vec), dim=1)
        user_prediction = self.fc_user_prediction(user_prediction_input)

        return torch.sigmoid(pos_features), torch.sigmoid(neg_features), duration_output, user_prediction
    
def contrastive_loss(pos_output, neg_output, margin=1.0):
    return torch.mean(torch.clamp(margin - (pos_output - neg_output), min=0.0))

def duration_loss(duration_output, true_durations):
    return nn.MSELoss()(duration_output.flatten(), true_durations)

def user_prediction_loss(user_prediction, true_user_ids):
    return nn.CrossEntropyLoss()(user_prediction, true_user_ids)

class DynamicLossWeights:
    def __init__(self, initial_weights):
        self.weights = initial_weights.float()

    def update_weights(self, losses):
        inverse_losses = torch.reciprocal(losses.float())
        total_inverse = torch.sum(inverse_losses)
        self.weights = (inverse_losses / total_inverse).float()


def train(model, dataloader, optimizer, loss_weights):
    for epoch in range(10):
        epoch_losses = []
        for user_ids, publisher_id, pos_texts, neg_texts, durations in dataloader:
            true_user_ids = publisher_id
            optimizer.zero_grad()

            pos_output, neg_output, duration_output, user_prediction = model(user_ids, publisher_id, pos_texts, neg_texts)
            
            loss_contrastive = contrastive_loss(pos_output, neg_output).float()
            loss_duration = duration_loss(duration_output, durations.float()).float()
            loss_user_prediction = user_prediction_loss(user_prediction, true_user_ids).float()

            total_loss = (loss_weights.weights[0] * loss_contrastive +
                        loss_weights.weights[1] * loss_duration +
                        loss_weights.weights[2] * loss_user_prediction)
            total_loss.backward()
            optimizer.step()

            epoch_losses.append(torch.tensor([loss_contrastive.item(), loss_duration.item(), loss_user_prediction.item()], dtype=torch.float32))
        
        epoch_losses_tensor = torch.stack(epoch_losses)
        mean_losses = torch.mean(epoch_losses_tensor, dim=0)
        loss_weights.update_weights(mean_losses)

        print(f'Epoch {epoch+1}, Loss: {total_loss.item()}, Weights: {loss_weights.weights.numpy()}')
    torch.save(model.state_dict(), '.\\cf-backend\\bert\\checkpoints\\model_10.pth')