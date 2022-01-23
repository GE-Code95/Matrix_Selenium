from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
import os
import json
import re


class BaseExtractor(webdriver.Firefox):
    DPATH = "C:/Program Files (x86)/geckodriver.exe"
    BPATH = "C:/Program Files/Mozilla Firefox/firefox.exe"

    def __init__(self, binary_location=BPATH, executable_path=DPATH):
        options = Options()
        options.headless = True
        options.binary_location = binary_location
        super().__init__(executable_path=executable_path, firefox_binary=binary_location, options=options)
        self.maximize_window()

    def previous_page(self):
        self.execute_script("window.history.go(-1)")

    def get_clickable(self, xpath):
        WebDriverWait(self, 15).until(
            EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def get_any_elements_by_xpath(self, xpath):
        WebDriverWait(self, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath)))

    def get_table(self, xpath):
        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))

    def get_element_text_by_xpath(self, xpath):
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element.text

    def get_correct_element(self, xpaths):
        for path in xpaths:
            try:
                correct = self.get_element_text_by_xpath(path)
                if correct is not None:
                    return correct
            except TimeoutException:
                print(f"{path} not found")
        # Throw exception about not finding any news headers
        raise

    def get_correct_element_content(self, xpaths):
        for path in xpaths:
            try:
                correct = self.get_elements_presence_by_xpath(path)
                if correct is not None:
                    return correct
            except TimeoutException:
                print(f"{path} not found")
        # Throw exception about not finding any news headers
        raise

    def get_elements_text_by_xpath(self, xpath):
        elements = WebDriverWait(self, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        lines = list(map(lambda element: element.text, elements))
        return '\n'.join(lines)

    def get_element_text_by_id(self, id):
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.ID, id)))
        return element.text

    def get_elements_presence_by_xpath(self, xpath):
        elements = WebDriverWait(self, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath)))
        lines = list(map(lambda element: element.text, elements))
        return '\n'.join(lines)

    def get_bbc_urls(self):
        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))

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
