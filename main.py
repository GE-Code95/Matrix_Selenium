from FlightExtractor import FlightExtractor
from NewsExtractor import NewsExtractor
from Summarizer import summarizer, sentiment_analyzer
import schedule
import time
import threading

stop_flag = False


class KeyboardThread(threading.Thread):

    def __init__(self, input_cbk=None, name='keyboard-input-thread'):
        self.input_cbk = input_cbk
        super(KeyboardThread, self).__init__(name=name)
        self.start()

    def run(self):
        while not stop_flag:
            self.input_cbk(input())  # waits to get input + Return


def keyboard_callback(inp):
    global stop_flag
    if inp.lower() == 'e':
        stop_flag = True


def main():
    """
    From here we run the two classes, in order to run one of them (of course) just comment the other one.

    NewsExtractor - After using get_data() change the path variable until saved_news to your machine.
    in search just type the expression you want and run it.
    to summarize and get sentiment analysis put the path.
    shutdown - closes firefox driver and all its instances (if exist).

    Flight Extractor - the table on the website is updated every 1 minute so I scheduled it to run every minute and
    get a fresh new table every time in order for it to stop hit E/e
    after it stopped you can use the search function exactly like NewsExtractor.
    shutdown - same as NewsExtractor
    """
    global stop_flag
    """
    news = NewsExtractor()
    news.get_data()
    # Put your path until saved_news folder
    path = r"C:/Users/Gil/PycharmProjects/Matrix_Selenium/saved_news"
    news.search(expression="Expression", filetype=".json", flag="news")
    summarizer(path)
    sentiment_analyzer(path)
    news.shutdown()"""

    flight = FlightExtractor()
    schedule.every(1).minutes.do(flight.get_data)
    print("Enter E/e to stop flights")
    kthread = KeyboardThread(keyboard_callback)
    while not stop_flag:
        schedule.run_pending()
        time.sleep(1)
    kthread.join()
    flight.search(expression='Expression', filetype='.json', flag="flights")
    flight.shutdown()


if __name__ == '__main__':
    main()
