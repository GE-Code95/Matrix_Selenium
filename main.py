from FlightExtractor import FlightExtractor
from NewsExtractor import NewsExtractor
from Summarizer import summarizer, sentiment_analyzer
import schedule
import time


def main():
    news = NewsExtractor()
    news.get_data()
    # Put your path until saved_news folder
    path = r"C:/Users/Gil/PycharmProjects/Matrix_Selenium/saved_news"
    news.search(expression="Expression", filetype=".json", flag="news")
    summarizer(path)
    sentiment_analyzer(path)
    news.shutdown()

    flight = FlightExtractor()
    schedule.every(1).minutes.do(flight.get_data)
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            break
    flight.search(expression='Expression', filetype='.json', flag="flights")
    flight.shutdown()


if __name__ == '__main__':
    main()
