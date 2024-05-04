import torch
from torch.utils.data import DataLoader
from bert.model import ContrastiveAndPredictiveModel, DynamicLossWeights, train
from bert.dataset import CustomDataset, collate_fn
import json
import random
from transformers import BertModel, BertTokenizer, BertConfig
import torch.nn.functional as F


def inference(model, tokenizer, publisher_id, description, top_k=10):
    model.eval()
    with torch.no_grad():
        publisher_tensor = torch.tensor([publisher_id], dtype=torch.long).to('cpu')

        
        pos_embedded = model.bert_model(**tokenizer(description, return_tensors='pt', padding=True, truncation=True, max_length=512))['last_hidden_state']  # Mean to reduce sequence dimension
        publisher_vec = model.publisher_embedding(publisher_tensor)
        
        pos_features = model.attention(pos_embedded, pos_embedded, pos_embedded)
        pos_features = pos_features.mean(dim=1)
        pos_features = F.leaky_relu(model.fc_info(pos_features))

        features = torch.cat((pos_features, publisher_vec), dim=1)


        user_prediction = model.fc_user_prediction(features)
        probabilities = torch.softmax(user_prediction, dim=1)

        top_probs, top_indices = torch.topk(probabilities, int(top_k))

        return top_indices.numpy(), top_probs.numpy()

def inference_user_ids(description, publisher_id, top_k=10):
    model_path = '.\\cf-backend\\bert\\checkpoints\\model_10.pth'
    model_state_dict = torch.load(model_path, map_location=torch.device('cpu'))

    model = ContrastiveAndPredictiveModel(num_users=60, embedding_size=64)
    model.load_state_dict(model_state_dict)

    tokenizer = BertTokenizer.from_pretrained('.\\cf-backend\\bert\\checkpoints\\bert')

    top_users, _ = inference(model, tokenizer, publisher_id, description, top_k)
    return top_users



if __name__ == "__main__":
    model_path = '.\\cf-backend\\bert\\checkpoints\\model_10.pth'
    model_state_dict = torch.load(model_path, map_location=torch.device('cpu'))

    model = ContrastiveAndPredictiveModel(num_users=60, embedding_size=64)
    model.load_state_dict(model_state_dict)

    tokenizer = BertTokenizer.from_pretrained('.\\cf-backend\\bert\\checkpoints\\bert')


    publisher_id = 1
    description = "我叫张小明，今年32岁，是一名普通的工程师。我的外婆叫李小丽，今年66岁，是一名普通的家庭主妇。她最近被诊断出患有严重的糖尿病，需要进行紧急的胰岛素治疗。我无法承担高昂的治疗费用，请您伸出援手，帮助我们渡过难关。"
    top_users, top_probs = inference(model, tokenizer, publisher_id, description)

    print("Top Users IDs:", top_users)
    for item in top_users[0]:
        print(int(item))
    print("Top Probabilities:", top_probs)
