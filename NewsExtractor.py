import time
from BaseExtractor import BaseExtractor
from Constants import POSSIBLE_CONTENT_XPATH, POSSIBLE_HEADERS_XPATH
from Summarizer import summarizer, sentiment_analyzer

URL = 'https://www.bbc.com/'


# TODO open news folder and put all parsed data to separate files | Fix search | Add summarizer features


class NewsExtractor(BaseExtractor):

    def __init__(self):
        super().__init__()

    def previous_page(self):
        self.execute_script("window.history.go(-1)")

    def get_data(self):
        ignore = ['sport', 'ideas', 'in-pictures']
        self.get(URL)
        self.get_bbc_urls()
        time.sleep(1)
        url_list = self.find_elements_by_css_selector("a.block-link__overlay-link")
        hrefs = [link.get_attribute('href') for link in url_list]

        for url in hrefs:
            print(url)
            if not any(domain in url for domain in ignore):
                self.get(url)
                header = self.get_correct_element(POSSIBLE_HEADERS_XPATH)
                content = self.get_correct_element_content(POSSIBLE_CONTENT_XPATH)
                print(header)
                print(content)

                self.previous_page()

    def search(self, expression, file_type='.txt'):
        self.search(expression, file_type)


def main():
    news = NewsExtractor()
    news.get_data()
    news.shutdown()

if __name__ == '__main__':
    main()
