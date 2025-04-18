# -*- coding: utf-8 -*-
"""NLP_Lab_2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fL0td0zAhgke3-lPkl3AyX-pQYtnMeGQ
"""

import re

def tokenize_and_detect_sentences(text):
    # Handle abbreviations
    text = re.sub(r"([A-Z]\.)+", lambda m: m.group(0).replace(".", ""), text)

    # Split text into potential sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][A-Z])(?<=\.|\?|\!)', text)

    # Tokenize words in each sentence
    tokenized_sentences = []
    for sentence in sentences:
        words = re.findall(r'\w+|[^\s\w]', sentence)
        tokenized_sentences.append(words)

    return tokenized_sentences

# Example usage
text = "Explore the universe today! What's beyond our galaxy? The U.S.A. and Canada are in North America."
tokenized_sentences = tokenize_and_detect_sentences(text)

for sentence in tokenized_sentences:
    print(" ".join(sentence))