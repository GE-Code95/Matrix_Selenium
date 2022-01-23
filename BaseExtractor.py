from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os
import json
import re

'''
url = 'https://www.bbc.com/'

driver.get(url)
actions = ActionChains(driver)

bbc_hrefs = []

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))
time.sleep(1)
media_list = driver.find_elements_by_css_selector("a.block-link__overlay-link")

for link in media_list:
    bbc_hrefs.append(link.get_attribute('href'))
    print(link.get_attribute('href'))


def previous():
    driver.execute_script("window.history.go(-1)")


for idx, url in enumerate(bbc_hrefs):
    if 'sport' not in url and 'news' in url:
        driver.get(url)
        header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "main-heading")))
        data_block = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component='text-block']")))
        print(header.text)
        for block in data_block:
            print(block.text)
        previous()
    else:
        if 'sport' not in url and 'news' not in url:
            driver.get(url)
            header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@tabindex='-1']")))

            intro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='article__intro b-font-family-serif']")))

            body = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//div/div/p")))
            print(header.text)
            print(intro.text)

            for p in body:
                print(p.text)

driver.close()
driver.quit()'''


class BaseExtractor(webdriver.Firefox):
    DPATH = "C:/Program Files (x86)/geckodriver.exe"
    BPATH = "C:/Program Files/Mozilla Firefox/firefox.exe"

    def __init__(self, binary_location=BPATH, executable_path=DPATH):
        options = Options()
        #options.headless = True
        options.binary_location = binary_location
        super().__init__(executable_path=executable_path, firefox_binary=binary_location, options=options)
        self.maximize_window()

    def previous_page(self):
        self.execute_script("window.history.go(-1)")

    def get_element_text_xpath(self, xpath):
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element.text

    def get_elements_text_xpath(self, xpath):
        elements = WebDriverWait(self, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        for element in elements:
            return element.text


    def get_data(self):
        raise NotImplementedError()

    def search(self, expression, filetype):
        pattern = fr'(\W{expression}\W)'
        dir_name = os.getcwd()
        ext = filetype
        for files in os.listdir(dir_name):
            if files.endswith(ext):
                f = open(files)
                data = json.load(f)
                search_result = re.search(pattern, data, flags=re.IGNORECASE)
                if search_result is not None:
                    print('Match found')
                else:
                    print('Match not found')
                f.close()
            else:
                continue

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()


if __name__ == '__main__':
    pass
