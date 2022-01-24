from FlightExtractor import FlightExtractor
from NewsExtractor import NewsExtractor
from Summarizer import summarizer, sentiment_analyzer
from textblob import TextBlob
import schedule

if __name__ == '__main__':
    """
    Instantiate NewsExtractor class
    """
    news = NewsExtractor()
    news.get_data()
    path = r"C:/Users/Gil/PycharmProjects/Matrix_Selenium/saved_news"
    news.search(expression="Expression", filetype=".json", flag="news")
    summarizer(path)
    sentiment_analyzer(path)
    news.shutdown()



