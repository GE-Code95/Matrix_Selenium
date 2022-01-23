import time
from BaseExtractor import BaseExtractor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = 'https://www.bbc.com/'
armadilo = 'https://www.bbc.com/news/uk-60083200'


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
    def get_data(self):
        ignore = ['sport', 'ideas', 'in-pictures']
        #self.get(URL)
        bbc_hrefs = []
        self.get(armadilo)
        header = WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        print(header.text)
        content = WebDriverWait(self, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div/p")))
        for p in content:
            print(p.text)

        '''
        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))
        time.sleep(1)
        media_list = self.find_elements_by_css_selector("a.block-link__overlay-link")

        for link in media_list:
            bbc_hrefs.append(link.get_attribute('href'))
            print(link.get_attribute('href'))

        for url in bbc_hrefs:
            #if ignore not in url and 'news' in url:
            if any(domain in url for domain in ignore):
                print(url)
                continue
            else:
                self.get(url)
                header = WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.ID, "main-heading")))
                data_block = WebDriverWait(self, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component='text-block']")))
                print(header.text)
                for block in data_block:
                    print(block.text)
                self.previous_page()
            else:
                if 'sport' not in url and 'news' not in url:
                    self.get(url)
                    header = WebDriverWait(self, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@tabindex='-1']")))

                    intro = WebDriverWait(self, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='article__intro b-font-family-serif']")))

                    body = WebDriverWait(self, 10).until(
                        EC.visibility_of_any_elements_located((By.XPATH, "//div/div/p")))
                    print(header.text)
                    print(intro.text)

                    for p in body:
                        print(p.text)'''

    def search(self, expression, file_type='.txt'):
        self.search(expression, file_type)


def main():
    news = NewsExtractor()
    news.get_data()


if __name__ == '__main__':
    main()
