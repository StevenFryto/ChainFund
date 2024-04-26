import torch
from torch.utils.data import Dataset
from datetime import datetime
import random
class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        entry = self.data[idx]
        user_id = int(entry["user_id"])
        publisher_id = int(entry["publisher_id"])
        positive_item = entry["description"]
        negative_item = random.choice([x["description"] for x in self.data if x["description"] != positive_item])
        
        # 将持续时间从 HH:MM:SS 转换为分钟
        duration = datetime.strptime(entry["duration"], "%H:%M:%S")
        duration_minutes = duration.hour * 60 + duration.minute + duration.second / 60
        
        return {
            "user_id": user_id,
            "publisher_id": publisher_id,
            "positive_item": positive_item,
            "negative_item": negative_item,
            "duration_minutes": duration_minutes
        }
    
def collate_fn(batch):
    user_ids = torch.tensor([item['user_id'] for item in batch], dtype=torch.long)
    publisher_ids = torch.tensor([item['publisher_id'] for item in batch], dtype=torch.long)
    pos_texts = [item['positive_item'] for item in batch]
    neg_texts = [item['negative_item'] for item in batch]
    durations = torch.tensor([item['duration_minutes'] for item in batch], dtype=torch.float)
    
    
    return user_ids, publisher_ids, pos_texts, neg_texts, durations