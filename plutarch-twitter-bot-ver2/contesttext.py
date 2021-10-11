import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class ContestText:

    def __init__(self, chrome_file_path, wikipedia_url, contestant_list):
        """ chrome_file_path: file path to chromedriver
            wikipedia_url:  a url for a wikipedia article with a table
            contestant_lists: a list of elements scrapped from a wikipedia table
            produces a dictionary with each element in contestant_name as the keys, and a summary of the corresponding
            article for each contestant name as the value
            """
        self.contestant_list = contestant_list
        self.driver = webdriver.Chrome(chrome_file_path)
        self.contestants_dict = {}
        for contestant_pair in self.contestant_list:
            for contestant in contestant_pair:
                self.driver.get(wikipedia_url)
                sleep(1)
                try:
                    link = self.driver.find_element_by_link_text(f'{contestant}')
                    sleep(1)
                    link.click()
                    sleep(1)
                    article_text = ''.join([paragraph.text for paragraph in self.driver.find_elements_by_css_selector("p")])
                    self.info = re.search(r'was(.*?)\.', article_text).group(1)
                    if len(self.info) > 120:
                        self.info = self.info[:120] + '...'
                    self.contestants_dict[contestant] = self.info
                except NoSuchElementException:
                    try:
                        link = self.driver.find_element_by_link_text(f'{contestant.split(" or")[0]}')
                        sleep(1)
                        link.click()
                        sleep(1)
                        article_text = \
                            ''.join([paragraph.text for paragraph in self.driver.find_elements_by_css_selector("p")])
                        self.info = re.search(r'was(.*?)\.', article_text).group(1)
                        if len(self.info) > 105:
                            self.info = self.info[:105] + '...'
                        self.contestants_dict[contestant] = self.info
                    except NoSuchElementException:
                        self.info = "No info found"
                        self.contestants_dict[contestant] = self.info







