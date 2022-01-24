from transformers import pipeline
from textblob import TextBlob
import json
import os


def summarizer(path):
    summarize = pipeline('summarization')
    for file in os.listdir(path):
        with open(f'{path}/{file}', 'r') as dict_file:
            content = json.loads(dict_file.read())["Content"]
            print(summarize(content, max_length=100, min_length=30, do_sample=False))


def sentiment_analyzer(path):
    for file in os.listdir(path):
        with open(f'{path}/{file}', 'r') as dict_file:
            content = json.loads(dict_file.read())["Content"]
        testimonial = TextBlob(content)
        print(testimonial.sentiment)
