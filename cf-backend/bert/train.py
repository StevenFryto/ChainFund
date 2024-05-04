import torch
from torch.utils.data import DataLoader
from model import ContrastiveAndPredictiveModel,DynamicLossWeights,train
from dataset import CustomDataset, collate_fn
import json
import random

# 定义一个函数，为单个数据项添加publisher属性
def add_publisher(data_item, user_id_to_avoid):
    # 假设publisher ID范围为001到100，除了要避免的user_id
    possible_ids = [f"{i:03}" for i in range(1, 51) if f"{i:03}" != user_id_to_avoid]
    
    # 为数据项添加一个随机选择的publisher ID
    data_item["publisher_id"] = random.choice(possible_ids)
    return data_item




def main():

    with open('D:\coding_program\Projects\ChainFund\cf-backend\\bert\data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    data = list(map(lambda item: add_publisher(item, item['user_id']), data))

    # 每个用户ID的样本数量
    n_samples_per_user = 500

    # 构造数据集实例
    dataset = CustomDataset(data)

    # 按用户ID分组样本
    grouped_data = {}
    for item in data:
        item["user_id"] = item["user_id"].replace('u', '')
        user_id = item["user_id"]
        if user_id in grouped_data:
            grouped_data[user_id].append(item)
        else:
            grouped_data[user_id] = [item]

    # 对每个用户ID的数据进行重采样
    resampled_data = []
    for user_id, items in grouped_data.items():
        if len(items) >= n_samples_per_user:
            sampled_items = random.sample(items, n_samples_per_user)
            resampled_data.extend(sampled_items)
        else:
            resampled_data.extend(items)

    dataset_resampled_data = CustomDataset(resampled_data)


    # 使用 collate_fn 函数创建 DataLoader
    dataloader = DataLoader(dataset_resampled_data, batch_size=30, shuffle=True, collate_fn=collate_fn)

    model = ContrastiveAndPredictiveModel(num_users=60, embedding_size=64)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    loss_weights = DynamicLossWeights(torch.tensor([0.25, 0.5, 0.25]))

    train(model, dataloader, optimizer, loss_weights)
    

if __name__ == "__main__":
    main()
