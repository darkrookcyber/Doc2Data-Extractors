import argparse
import re

def clean_text(text):
    """
    Pre-processes the given text by removing special characters, extra spaces, and lowercasing the text.
    
    Args:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned text.
    """
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Convert to lowercase
    text = text.lower().strip()
    return text

def tokenize(text):
    """
    Tokenizes the text by splitting on whitespace.

    Args:
    text (str): The text to be tokenized.

    Returns:
    list of str: A list of tokens.
    """
    return text.split()

def process_file(input_file_path):
    """
    Processes the input text file, cleaning and tokenizing the text, and writes the tokenized data to an output file.

    Args:
    input_file_path (str): The path to the input text file.
    """
    # Define the output file path
    output_file_path = input_file_path.rsplit('.', 1)[0] + '_tokenized.txt'

    with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            cleaned_line = clean_text(line)
            tokens = tokenize(cleaned_line)
            output_file.write(' '.join(tokens) + '\n')

    print(f"Tokenized data has been written to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pre-process and tokenize text data for Mistral model training.")
    parser.add_argument("input_file", nargs='?', help="The path to the input text file containing unstructured data.")
    args = parser.parse_args()

    input_file_path = args.input_file
    if not input_file_path:
        input_file_path = input("Please enter the path to the input text file: ")

    process_file(input_file_path)