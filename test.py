# from selenium import webdriver
#
# options = webdriver.chrome.options.Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-setuid-sandbox")
# options.add_argument("--disable-extensions")
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(options=options)
#
# driver.get("https://httpstat.us/200")
#
# if "200 OK" in driver.page_source:
#     print('Selenium successfully opened with Chrome (under the Xvfb display) and navigated to "https://httpstat.us/200", you\'re all set!')

import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By



class GoogleReviews:

    def __init__(self):
        self.review_url = 'https://www.google.com/maps/place/%D0%A3%D0%BB%D1%83%D1%83-%D0%A2%D0%BE%D0%BE/@42.8834923,74.5868375,15.77z/data=!4m5!3m4!1s0x389ec933bd943621:0x18ab7a9e283eaf18!8m2!3d42.8844016!4d74.5792839'
        # self.review_url = review_url
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.options = uc.ChromeOptions()
        self.options.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox"])
        self.driver = uc.Chrome(use_subprocess=True, options=self.options)

    def get_page(self):
        self.driver.get(self.url)

    def login(self, email, password):
        # logger.info('Google login ')
        print('Google login')
        self.wait_element_for_send(self.driver, By.NAME, 'identifier', 'valerija.korolevat2nd0@gmail.com')
        time.sleep(5)
        self.wait_element_for_click(self.driver, By.ID, 'identifierNext')
        # logger.info('Google enter email  ')
        time.sleep(5)
        self.wait_element_for_send(self.driver, By.NAME, 'Passwd', 'W6r4YejgMoRh7vu')
        time.sleep(5)
        self.wait_element_for_click(self.driver, By.ID, 'passwordNext')
        print('Google enter password ')

    def wait_element_for_send(self,driver, by, element, data):
        attempts = 20
        while attempts:
            try:
                input_email = driver.find_element(by, element)
                input_email.send_keys(data)
                # logger.info('Send data')
                return True
            except:
                # logger.error('Error while sending ')
                attempts -= 1
                time.sleep(1)
        raise 'Error while wait_element_for_send'

    def wait_element_for_click(self,driver, by, element):
        attempts = 20
        while attempts:
            try:
                input_email = driver.find_element(by, element)
                input_email.click()
                # logger.info('Click on button')
                return True
            except:
                # logger.error('Error while click on button')
                attempts -= 1
                time.sleep(1)
        raise 'Error while wait_element_for_click'

if __name__ == "__main__":
    obj = GoogleReviews()
    time.sleep(5)
    obj.get_page()
    time.sleep(5)
    obj.login()
    print('Account login 200')