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
        try:
            human_msg = self.driver.find_element_by_xpath('/html/body/section/div[2]/div/h1')
            print("Warning: robot detection. ")
            input("Press Enter to continue script...")
        except:
            pass
        login_page_btn = self.driver.find_element_by_xpath('/html/body/div[2]/header/div[3]/div[3]/a[2]')
        login_page_btn.click()
        sleep(1)
        email_in = self.driver.find_element_by_xpath('/html/body/div[7]/auth-layout/div/div/div[2]/ui-view/login/div/div[4]/form/div[1]/input')
        email_in.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('/html/body/div[7]/auth-layout/div/div/div[2]/ui-view/login/div/div[4]/form/div[2]/input')
        pw_in.send_keys(password)
        sleep(1)
        login_btn = self.driver.find_element_by_xpath('/html/body/div[7]/auth-layout/div/div/div[2]/ui-view/login/div/div[4]/eo-button/button/span/span')
        login_btn.click()
        sleep(1)

        # login: /html/body/div[2]/header/div[3]/div[3]/a[2]
        # mail: /html/body/div[7]/auth-layout/div/div/div[2]/ui-view/login/div/div[4]/form/div[1]/input
        # pass: /html/body/div[7]/auth-layout/div/div/div[2]/ui-view/login/div/div[4]/form/div[2]/input
        # login btn: /html/body/div[7]/auth-layout/div/div/div[2]/ui-view/login/div/div[4]/eo-button/button/span/span
        # first button: /html/body/div[2]/header/div[3]/ul/li[1]/a
        # history: /html/body/div[2]/header/div[3]/ul/li[1]/ul/li[2]/a
        # t1: /html/body/div[7]/ui-view/div/div/div/div[2]/div[1]/ul[2]/li[1]/ng-include/a/div[2]/eo-workout-cell/div/div/div[2]/div[2]
        #     /html/body/div[7]/ui-view/div/div/div/div[2]/div[1]/ul[2]/li[8]/ng-include/a/div[2]/eo-workout-cell/div/div/div[2]/div[2]
        # t2: /html/body/div[7]/ui-view/div/div/div/div[2]/div[1]/ul[2]/li[2]/ng-include/a/div[2]/eo-workout-cell/div/div/div[2]/div[1]
        # t3: /html/body/div[7]/ui-view/div/div/div/div[2]/div[1]/ul[2]/li[3]/ng-include/a/div[2]/eo-workout-cell/div/div/div[2]/div[2]
        # export button 01: /html/body/div[7]/ui-view/div[2]/div[3]/div[1]/div/div[2]/ul/li[12]
        # modal window: /html/body/div[13]/div/div/div/div
        # gpx format: /html/body/div[13]/div/div/div/form/div[1]/div/div[2]/div/label
        # export button: /html/body/div[13]/div/div/div/form/div[2]/a

        return

    def download_tracks(self, skip_counter=0):
        self.driver.get('https://www.endomondo.com/users/2944579/history')
        print('Will skip', skip_counter, 'trainings')
        while True:
            for i in range(1, 21):
                if skip_counter > 0:
                    skip_counter -= 1
                else:
                    sleep(2)
                    train_xpath = '/html/body/div[7]/ui-view/div/div/div/div[2]/div[1]/ul[2]/li[' + str(i) + ']/ng-include/a/div[2]/eo-workout-cell/div/div/div[2]/div[2]'
                    try:
                        train_btn = self.driver.find_element_by_xpath(train_xpath)
                    except NoSuchElementException:
                        print('Message: End element in the track list')
                        input("Press Enter to continue script...")
                        return
                    # Open the link in a new tab by sending key strokes on the element
                    train_btn.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    self._download_gpx()
                    # Close current tab
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
        pass

    def _download_gpx(self):
        print("Process train")
        input("Press Enter to continue script...")
        pass
