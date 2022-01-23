from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA

text = '''
   I had a mixed day, in the morning it was good and in the evening it was horrible, I hope it will be better tomorrow
    '''


def summarizer():
    summarize = pipeline('summarization')
    print(summarize(text, max_length=100, min_length=30, do_sample=False))


def sentiment_analyzer(file):
    sia = SIA()
    for sentence in file:
        ss = sia.polarity_scores(sentence)
    return ss


if __name__ == '__main__':
    some_file = 'x'
    sentiment_analyzer(some_file)
