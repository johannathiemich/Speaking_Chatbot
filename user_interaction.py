import os
import sys
import errno
import nltk
import numpy as np
from string import punctuation
import logging
import speech_recognition as sr

from speech_processing import EasySpeechHandler


def preprocess(data_path):
    if os.path.isfile(data_path):
        file = open(data_path, 'r', errors='ignore')
        raw = file.read()

        sent_tokens = nltk.sent_tokenize(raw, language='german')
        word_tokens = nltk.word_tokenize(raw, language='german')
        cistem = nltk.stem.cistem.Cistem()
        lemmer = map(cistem.stem, word_tokens)
        lem_words = set(lemmer)
        without_punct = [string if string not in punctuation else '' for string in lem_words]
        without_punct_clean = [string for string in without_punct if string]
        return without_punct_clean
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), data_path)



def main():
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    preprocess("example.txt")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    speech_handler = EasySpeechHandler()
    input = preprocess(speech_handler.recognize(audio_data=audio))

if __name__ == "__main__":
    main()
