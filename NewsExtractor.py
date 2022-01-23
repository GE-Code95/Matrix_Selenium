import time
from BaseExtractor import BaseExtractor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = 'https://www.bbc.com/'


class NewsExtractor(BaseExtractor):

    def __init__(self):
        super().__init__()

    def previous_page(self):
        self.execute_script("window.history.go(-1)")

    '''
    types of articles:
    1) normal news
    2) news with different structure
    3) culture/travel/future/work-life
    4) food
    5) in pictures
    5) ideas
    '''

    @staticmethod
    def split_url_list(url_list):
        '''
        :param url_list: a list of all the hrefs from the main BBC website
        :return: two lists, one with /news and all the other types such as future, art etc.
        '''
        news_only = [url for url in url_list if 'news' in url]
        others = [url for url in url_list if 'news' not in url]

        return news_only, others

    def get_data(self):
        ignore = ['sport', 'ideas', 'in-pictures']
        self.get(URL)
        self.get_bbc_urls()
        time.sleep(1)
        url_list = self.find_elements_by_css_selector("a.block-link__overlay-link")

        hrefs = [link.get_attribute('href') for link in url_list]
        news, others = self.split_url_list(hrefs)
        print(news)
        print(others)

        for url in hrefs:
            # if ignore not in url and 'news' in url:
            if any(domain in url for domain in ignore):
                print(url)
                continue
            else:
                self.get(url)
                header = self.get_element_text_by_id("//*[@id='main-heading']")
                data_block = self.get_elements_presence_by_xpath("//*[@id='main-content']//article/div//p")
                print(header)
                print(data_block)
                self.previous_page()
            '''
        self.get_bbc_urls()
        time.sleep(1)
        url_list = self.find_elements_by_css_selector("a.block-link__overlay-link")

        for link in url_list:
            all_urls.append(link.get_attribute('href'))
            print(link.get_attribute('href'))

        for url in all_urls:
            if 'sport' not in url and 'news' not in url:
                self.get(url)
                header = self.get_element_text_by_xpath("//div[@tabindex='-1']")
                intro = self.get_element_text_by_xpath("//div[@class='article__intro b-font-family-serif']")
                body = self.get_any_elements_by_xpath("//div/div/p")
                print(header)
                print(intro)
                print(body)

    def search(self, expression, file_type='.txt'):
        self.search(expression, file_type)
        '''


def main():
    news = NewsExtractor()
    news.get_data()


if __name__ == '__main__':
    main()
