import os
from collections import OrderedDict
import re

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()

# Function to clean a text file and save the unique words while preserving order
def clean_text_file(input_file_path, output_file_path):
    unique_words = OrderedDict()
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

        # Use regular expression to split content into words while preserving punctuation
        words = re.findall(r'\b\w+\b', content)

        for word in words:
            word = word.lower()  # Convert the word to lowercase
            unique_words[word] = None

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(' '.join(unique_words.keys()))

# Iterate through all .txt files in the script's directory
for filename in os.listdir(script_dir):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(script_dir, filename)
        output_file_path = os.path.join(script_dir, f'cleaned_{filename}')
        clean_text_file(input_file_path, output_file_path)
        print(f"Cleaned text saved to {output_file_path}")
