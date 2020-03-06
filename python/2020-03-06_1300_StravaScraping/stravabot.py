import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep


class StravaBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def close_browser(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.get('https://www.strava.com/')
        login_page_btn = self.driver.find_element_by_xpath('//*[@id="view"]/header/div/nav/a')
        login_page_btn.click()
        sleep(1)
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        pw_in.send_keys(password)
        sleep(1)
        login_btn = self.driver.find_element_by_xpath('//*[@id="login-button"]')
        login_btn.click()
        if 'login' in self.driver.current_url:
            raise Exception('login failed - authentication error')

    def download_tracks(self, skip_counter=0):
        self.driver.get('https://www.strava.com/athlete/training')
        print('Will skip', skip_counter, 'trainings')
        while True:
            for i in range(1, 21):
                if skip_counter > 0:
                    skip_counter -= 1
                else:
                    sleep(2)
                    train_xpath = '//*[@id="search-results"]/tbody/tr[' + str(i) + ']/td[3]/a'
                    try:
                        train_btn = self.driver.find_element_by_xpath(train_xpath)
                    except NoSuchElementException:
                        print('Message: End element in the track list')
                        return
                    # Open the link in a new tab by sending key strokes on the element
                    train_btn.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)
                    self.driver.switch_to_window(self.driver.window_handles[1])
                    self._download_gpx()
                    # Close current tab
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
            try:
                sleep(2)
                next_train_page_btn = self.driver.find_element_by_xpath('/html/body/div[3]/nav/div/ul/li[2]/button')
                next_train_page_btn.click()
            except NoSuchElementException:
                print('Message: Latest track list')
                return

    def _download_gpx(self):
        sleep(0.5)
        track_name = self.driver.find_element_by_xpath('//*[@id="heading"]/div/div/div[1]/div/div/h1')
        try:
            btn01 = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/nav/div/div/div')
            btn01.click()
            sleep(0.5)
            export_gpx_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/nav/div/div/ul/li[7]/a')
            export_gpx_btn.click()
        except Exception as e:
            print('Error: downloading gpx:', track_name.text, "Unexpected error:", str(e))
