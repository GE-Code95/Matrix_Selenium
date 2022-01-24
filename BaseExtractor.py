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
    """
     The BaseExtractor class contains the base of each extractor and gives its functionality
    """
    DPATH = "C:/Program Files (x86)/geckodriver.exe"
    BPATH = "C:/Program Files/Mozilla Firefox/firefox.exe"

    def __init__(self, binary_location=BPATH, executable_path=DPATH):
        """
        Initialize new extractor object, using headless mode for speed,
        and maximizing window for full data to be extracted.

        :param binary_location: path to the binaries of Firefox
        :param executable_path: path to the webdriver to be executed
        """
        options = Options()
        options.headless = True
        options.binary_location = binary_location
        super().__init__(executable_path=executable_path, firefox_binary=binary_location, options=options)
        self.maximize_window()

    def previous_page(self):
        """
        A simple function to execute script to go back to the previous page.
        """
        self.execute_script("window.history.go(-1)")

    def get_clickable(self, xpath):
        """
        :param xpath: the XPath string to be found
        :return: clickable WebElement object
        """
        WebDriverWait(self, 15).until(
            EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def get_any_elements_by_xpath(self, xpath):
        """
        find any elements specified by the XPath string
        :param xpath: the XPath string to be found
        :return: all WebElement objects related.
        """
        return WebDriverWait(self, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath)))

    def get_table(self, xpath):
        """
        get table after all rows have been shown
        :param xpath: the XPath string to be found
        :return: all WebElement objects related which are visible.
        """
        return WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))

    def get_element_text_by_xpath(self, xpath):
        """
        gets a string by using the element.text attribute
        :param xpath: the XPath string to be found
        :return: string according to XPath search
        """
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element.text

    def get_elements_text_by_xpath(self, xpath):
        """
        gets a string by using the element.text attribute
        :param xpath: the XPath strings to be found
        :return: strings according to XPath search
        """
        elements = WebDriverWait(self, 10).until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        lines = list(map(lambda element: element.text, elements))
        return '\n'.join(lines)

    def get_correct_element(self, xpaths):
        """
        used for the header object extraction, tries to determine to which XPath it belongs and then extracts it
        :param xpaths: list of XPaths to be checked
        :return: correct element to be extracted
        """
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
        """
        used for the content object extraction, tries to determine to which XPath it belongs and then extracts it
        :param xpaths: list of XPaths to be checked
        :return: correct element to be extracted as content
        """
        for path in xpaths:
            try:
                correct = self.get_elements_presence_by_xpath(path)
                if correct is not None:
                    return correct
            except TimeoutException:
                print(f"{path} not found")
        # Throw exception about not finding any news headers
        raise

    def get_element_text_by_id(self, id):
        """
        gets a string by using the element.text attribute
        :param xpath: the ID attribute to be found
        :return: strings according to the given HTML ID
        """
        element = WebDriverWait(self, 10).until(EC.visibility_of_element_located((By.ID, id)))
        return element.text

    def get_elements_presence_by_xpath(self, xpath):
        """
        looking for presence of elements by XPat
        :param xpath: the XPath strings to be found
        :return: strings according to the given XPath
        """
        elements = WebDriverWait(self, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath)))
        lines = list(map(lambda element: element.text, elements))
        return '\n'.join(lines)

    def get_bbc_urls(self):
        """
        gets all BBC hrefs.
        :return: list of all main articles in the BBC website
        """
        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.block-link__overlay-link")))

    def get_data(self):
        """
        Implemented in each class - getting data according the class
        """
        raise NotImplementedError()

    def search(self, expression, filetype, flag):
        """
        by using regex we search for give word or words
        :param flag: which type of directory
        :param expression: the expression to be found
        :param filetype: the type of file we are searching
        :return: match found or not
        """
        pattern = fr'(\W{expression}\W)'
        dir_name = os.getcwd() + f"/saved_{flag}"
        ext = filetype
        for files in os.listdir(dir_name):
            if files.endswith(ext):
                f = open(files)
                data = json.load(f)
                search_result = re.search(pattern, data, flags=re.IGNORECASE)
                if search_result is not None:
                    print(f'Match found in file {files}')
                else:
                    print('Match not found')
                f.close()
            else:
                continue

    def store_data(self, data_file):
        """
        Implemented in each class - storing the data to the file system.
        """
        raise NotImplementedError()

    def shutdown(self):
        "Terminate all instances and quits the webdriver"
        self.close()
        self.quit()
