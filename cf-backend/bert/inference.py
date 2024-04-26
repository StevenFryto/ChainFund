import torch
from torch.utils.data import DataLoader
from model import ContrastiveAndPredictiveModel, DynamicLossWeights, train
from dataset import CustomDataset, collate_fn
import json
import random
from transformers import BertModel, BertTokenizer, BertConfig
import torch.nn.functional as F


def inference(model, tokenizer, publisher_id, description, top_k=10):
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():  # No gradient needed
        # Prepare the inputs
        publisher_tensor = torch.tensor([publisher_id], dtype=torch.long).to('cpu')

        
        # Get embeddings
        pos_embedded = model.bert_model(**tokenizer(description, return_tensors='pt', padding=True, truncation=True, max_length=512))['last_hidden_state']  # Mean to reduce sequence dimension
        publisher_vec = model.publisher_embedding(publisher_tensor)
        
        # Combine and process embeddings
        pos_features = model.attention(pos_embedded, pos_embedded, pos_embedded)
        pos_features = pos_features.mean(dim=1)  # Mean to reduce sequence dimension
        pos_features = F.leaky_relu(model.fc_info(pos_features))
        # Merge description and publisher info before prediction
        features = torch.cat((pos_features, publisher_vec), dim=1)

        # Predict user probabilities
        user_prediction = model.fc_user_prediction(features)

        # Apply softmax to get probabilities
        probabilities = torch.softmax(user_prediction, dim=1)

        # Retrieve top k probabilities and their corresponding indices
        top_probs, top_indices = torch.topk(probabilities, top_k)

        return top_indices.numpy(), top_probs.numpy()

# Example usage
if __name__ == "__main__":
    # Load the model and tokenizer
    model_path = './checkpoints/model_1.pth'  # Adjust to your model path
    model_state_dict = torch.load(model_path, map_location=torch.device('cpu'))

    model = ContrastiveAndPredictiveModel(num_users=10000, embedding_size=64)  # Ensure these parameters match training
    model.load_state_dict(model_state_dict)

    tokenizer = BertTokenizer.from_pretrained('./checkpoints/bert/')

    # Example of inference
    publisher_id = 1  # Sample publisher ID
    description = "我叫张小明，今年32岁，是一名普通的工程师。我的外婆叫李小丽，今年66岁，是一名普通的家庭主妇。她最近被诊断出患有严重的糖尿病，需要进行紧急的胰岛素治疗。我无法承担高昂的治疗费用，请您伸出援手，帮助我们渡过难关。"  # Example project description
    top_users, top_probs = inference(model, tokenizer, publisher_id, description)

    print("Top Users IDs:", top_users)
    print("Top Probabilities:", top_probs)
