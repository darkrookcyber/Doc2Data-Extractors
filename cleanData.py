"""
Name: cleandata.py
Use: performs basic cleaning on a text file, needs textblob library
pip3 install textblob

CLI Use: python3 cleanData.py inputfile.txt

"""


import sys
import os
from textblob import TextBlob

def clean_text(input_file):
    # Define the output file path
    output_file = os.path.join(os.path.dirname(input_file), 'cleantext.txt')

    try:
        with open(input_file, 'r') as file:
            text = file.read()

        # Remove unnecessary whitespace
        text = ' '.join(text.split())

        # Correct obvious typos using TextBlob
        blob = TextBlob(text)
        corrected_text = str(blob.correct())

        with open(output_file, 'w') as file:
            file.write(corrected_text)

        print(f"Cleaned text has been saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        input_file = sys.argv[1]
        clean_text(input_file)