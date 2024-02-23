"""
Name: uploadData.py
Description:
This script will upload formatted data into the Mistral model for fine-tuning or inference, this program assumes you're using PyTorch and that your formatted data is in a CSV file with two columns: text and label.

Use:
	pip3 install torch transformers pandas
	python3 uploadData.py --model_path /path/to/mistral/model --data_path /path/to/formatted/formatted_data.csv
	
	
Examples for pasting:

---
chat template
tokenizer.chat_template = "{% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{% for message in messages %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}"


"""

import argparse
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, filename, tokenizer, max_len=512):
        self.data = pd.read_csv(filename)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        text = self.data.iloc[index]['text']
        inputs = self.tokenizer.encode_plus(
            text,
            None,
            add_special_tokens=True,
            max_length=self.max_len,
            padding='max_length',
            return_token_type_ids=False,
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        return {
            'input_ids': inputs['input_ids'].flatten(),
            'attention_mask': inputs['attention_mask'].flatten()
        }

def load_data_and_model(model_path, data_path):
    print(f"Loading model from {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)

    print(f"Loading data from {data_path}")
    dataset = CustomDataset(data_path, tokenizer)
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

    return model, dataloader

def main(model_path, data_path):
    model, dataloader = load_data_and_model(model_path, data_path)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    print("Starting inference...")
    model.eval()
    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask)
            print(outputs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load formatted data into Mistral model for processing.")
    parser.add_argument('--model_path', type=str, help='Path to the Mistral model.')
    parser.add_argument('--data_path', type=str, help='Path to the formatted data CSV file.')

    args = parser.parse_args()

    if args.model_path and args.data_path:
        main(args.model_path, args.data_path)
    else:
        print("No command line input provided. Please enter the required paths.")
        model_path = input("Enter the path to the Mistral model: ").strip()
        data_path = input("Enter the path to the formatted data CSV file: ").strip()
        main(model_path, data_path)