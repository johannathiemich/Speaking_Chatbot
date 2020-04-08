import os
import nltk
import numpy as np
import string

def preprocess(data_path):
    if os.path.isfile(data_path):
        file = open(data_path, 'r', errors='ignore')
        raw = file.read()

        sent_tokens = nltk.sent_tokenize(raw, language='german')
        word_tokens = nltk.word_tokenize(raw, language='german')
        lemmer = map(nltk.stem.cistem.Cistem.stem, word_tokens)
        lem_words = set(lemmer)
        print(lem_words)


def main():
    preprocess("example.txt")


if __name__ == "__main__":
    main()
