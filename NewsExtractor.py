import time
from BaseExtractor import BaseExtractor
from Constants import POSSIBLE_CONTENT_XPATH, POSSIBLE_HEADERS_XPATH
import os
import json

URL = 'https://www.bbc.com/'


class NewsExtractor(BaseExtractor):

    def __init__(self):
        """
            Initialize NewsExtractor Class calling super
        """
        super().__init__()

    def previous_page(self):
        """
        Go back to te previous page.
        """
        self.execute_script("window.history.go(-1)")

    def store_data(self, saved_file):
        """
        After extraction store the data in the file system.
        :param saved_file: the file to be saved to the system
        """
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
        """
        the main function to extract the data parsing table names and its contents.
        """
        # Ignore the urls NOT containing articles
        ignore = ['sport', 'ideas', 'in-pictures']
        self.get(URL)
        self.get_bbc_urls()
        time.sleep(1)
        # Get all the URL elements
        url_list = self.find_elements_by_css_selector("a.block-link__overlay-link")
        # Get href attribute
        hrefs = [link.get_attribute('href') for link in url_list]

        for url in hrefs:
            if not any(domain in url for domain in ignore):
                self.get(url)
                # header and content look for the right XPath, when found it is extracted
                header = self.get_correct_element(POSSIBLE_HEADERS_XPATH)
                content = self.get_correct_element_content(POSSIBLE_CONTENT_XPATH)
                # after capturing the data we save it in this format including the URL as requested
                data = {"Header": f"{header}", "URL": f"{url}", "Content": f'{content}'}
                self.store_data(data)
                self.previous_page()
