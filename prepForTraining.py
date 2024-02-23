"""
Name: prepForTraining.py
Description:  
For training GPT-2 mistral models, especially in tasks related to analyzing company data, it's often beneficial to compile data from multiple sources/companies into a single dataset, provided that each entry is labeled correctly. This approach allows the model to learn from a broader range of examples and generalize better across different companies.

Given this, this script will:

	Take multiple clean text datasets as input.
	Assign a label to each dataset, which could be the company name or a specific identifier you choose.
	Combine all datasets into a single CSV file with proper labeling. 

Use:
	pip3 install pandas
	pip3 install Pyarrow
	python3 prepForTraining.py --files /path/to/company1.txt /path/to/company2.txt --labels Company1 Company2 --output combined_data.csv

"""

import argparse
import pandas as pd
import os

def prepare_data(files, labels, output_dir):
    combined_data = []

    for file_path, label in zip(files, labels):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    text = line.strip()
                    if text:  # Ensure the line is not empty
                        combined_data.append({'text': text, 'label': label})

        except Exception as e:
            print(f"An error occurred while processing {file_path}: {e}")

    if combined_data:
        output_file = os.path.join(output_dir, 'formatted_data.csv')
        df = pd.DataFrame(combined_data)
        df.to_csv(output_file, index=False)
        print(f"Formatted data saved to {output_file}")
    else:
        print("No data was formatted.")

def main():
    parser = argparse.ArgumentParser(description="Prepare text data from multiple companies for training.")
    parser.add_argument('--files', nargs='*', help='Paths to the clean text files.')
    parser.add_argument('--labels', nargs='*', help='Labels for each file (e.g., company names).')

    args = parser.parse_args()

    if args.files and args.labels:
        if len(args.files) != len(args.labels):
            print("Error: The number of files must match the number of labels.")
            return
        output_dir = os.path.dirname(args.files[0])
        prepare_data(args.files, args.labels, output_dir)
    else:
        files, labels = get_user_input()
        if files and labels:
            output_dir = os.path.dirname(files[0])
            prepare_data(files, labels, output_dir)
        else:
            print("No input provided.")

def get_user_input():
    files = []
    labels = []

    print("Enter the paths to your text files, followed by their labels. Type 'done' when finished.")
    while True:
        file_path = input("File path: ").strip()
        if file_path.lower() == 'done':
            break
        label = input("Label for this file: ").strip()
        files.append(file_path)
        labels.append(label)

    return files, labels

if __name__ == "__main__":
    main()
