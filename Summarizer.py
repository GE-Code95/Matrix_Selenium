from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

text = '''
   I had a mixed day, in the morning it was good and in the evening it was horrible, I hope it will be better tomorrow
    '''


def summarizer():
    summarizer = pipeline('summarization')

    print(summarizer(text, max_length=100, min_length=30, do_sample=False))


def sentiment_analyzer():
    obj = SentimentIntensityAnalyzer()
    print(obj.polarity_scores(text))


if __name__ == '__main__':
    sentiment_analyzer()
