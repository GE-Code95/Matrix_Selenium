import time
from BaseExtractor import BaseExtractor
from Constants import POSSIBLE_CONTENT_XPATH, POSSIBLE_HEADERS_XPATH
from Summarizer import summarizer, sentiment_analyzer, text_blob
import os
import json

URL = 'https://www.bbc.com/'


class NewsExtractor(BaseExtractor):

    def __init__(self):
        super().__init__()

    def previous_page(self):
        self.execute_script("window.history.go(-1)")

    def store_data(self, saved_file):
        file_name = (list(saved_file.values())[0])
        directory = 'saved_news'
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        file_path = f'{path}\\{file_name.replace(":", "")}'.replace(" ", "_").replace("?", "")
        with open(f'{file_path}.json', "w+") as file:
            json.dump(saved_file, file)

    def get_data(self):
        ignore = ['sport', 'ideas', 'in-pictures']
        self.get(URL)
        self.get_bbc_urls()
        time.sleep(1)
        url_list = self.find_elements_by_css_selector("a.block-link__overlay-link")
        hrefs = [link.get_attribute('href') for link in url_list]

        for url in hrefs:
            if not any(domain in url for domain in ignore):
                self.get(url)
                header = self.get_correct_element(POSSIBLE_HEADERS_XPATH)
                content = self.get_correct_element_content(POSSIBLE_CONTENT_XPATH)
                data = {"Header": f"{header}", "URL": f"{url}", "Content": f'{content}'}
                self.store_data(data)
                self.previous_page()


def main():
    news = NewsExtractor()
    # news.get_data()
    #summarizer(r"C:/Users/Gil/PycharmProjects/Matrix_Selenium/saved_news")
    # news.search(expression="Expression", filetype=".json", flag="news")
    #sentiment_analyzer(r"C:/Users/Gil/PycharmProjects/Matrix_Selenium/saved_news")
    text_blob(r"C:/Users/Gil/PycharmProjects/Matrix_Selenium/saved_news")
    news.shutdown()


if __name__ == '__main__':
    main()
