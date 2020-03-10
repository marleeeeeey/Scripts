import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep


class EndomondoBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def close_browser(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.get('https://www.endomondo.com/')
        return

    def download_tracks(self, skip_counter=0):
        pass

    def _download_gpx(self):
        pass
