from FlightExtractor import FlightExtractor
from NewsExtractor import NewsExtractor
from Summarizer import summarizer, sentiment_analyzer
import schedule

if __name__ == '__main__':
    """
    Instantiate NewsExtractor class
    """
    news = NewsExtractor()
    news.get_data()
    news.search(expression="Expression", filetype=".json", flag="news")
    summarizer(r"C:/Users/Gil/PycharmProjects/Matrix_Selenium/saved_news")
    #sentiment_analyzer()
    news.shutdown()
    """
       Instantiate FlightsExtractor class
    """
    flight = FlightExtractor()
    schedule.every(1).minutes.do(flight.get_data)
    '''
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            break
            '''
    flight.get_data()
    flight.search(expression="Expression", filetype=".json", flag="flights")
    flight.shutdown()

