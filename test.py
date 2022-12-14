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
        self.review_url = 'https://www.google.com/maps/place/%D0%A0%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD+%D0%9A%D0%90%D0%A3%D0%A1%D0%90%D0%A0/@42.8915112,74.5909522,14.21z/data=!4m13!1m7!3m6!1s0x389ec7ffb9cbd6b9:0x9616d4cf9871ceda!2z0JjRhdC70LDRgSwg0J_RgNC-0YTQtdGB0YHQvtGA0LAg0JfQuNC80YssINCR0LjRiNC60LXQug!3b1!8m2!3d42.8978824!4d74.5912702!3m4!1s0x0:0x9cf6f753310c0704!8m2!3d42.8853328!4d74.6142781'
        # self.review_url = review_url
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.options = uc.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-setuid-sandbox")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-dev-shm-usage")

        # self.options.arguments.extend(["--no-sandbox", "--disable-setuid-sandbox", '--disable-dev-shm-usage', '--disable-extensions'])
        self.driver = uc.Chrome(use_subprocess=True, options=self.options)

    def get_page(self):
        self.driver.get(self.url)

    def login(self):
        # logger.info('Google login ')
        print('Google login')
        time.sleep(3)
        print(self.driver.find_element(By.XPATH, '//*[@id="headingSubtext"]/span').text)
        time.sleep(10)

        self.wait_element_for_send(self.driver, By.NAME, 'identifier', 'valerija.korolevat2nd0@gmail.com')
        time.sleep(5)
        self.wait_element_for_click(self.driver, By.ID, 'identifierNext')
        # logger.info('Google enter email  ')
        time.sleep(5)
        self.wait_element_for_send(self.driver, By.NAME, 'Passwd', 'W6r4YejgMoRh7vu')
        time.sleep(5)
        self.wait_element_for_click(self.driver, By.ID, 'passwordNext')
        print('Google enter password ')
        time.sleep(10)
        text = self.driver.find_element(By.XPATH,
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/h1').text
        print(text)
    def get_review_page(self):
        self.driver.get(self.review_url)
        print('entered to rieviews url')

        time.sleep(5)

    def open_review(self):
        time.sleep(10)
        buttons = self.driver.find_elements(By.CLASS_NAME, 'S9kvJb')
        # print(self.driver.find_element(By.XPATH, '//*[@id="headingSubtext"]/span').text)
        # logger.info('Google login ')
        # logger.info('Open google maps')
        print('open google maps')
        time.sleep(5)
        # language = self.driver.execute_script("return window.navigator.userLanguage || window.navigator.language")
        # logger.info(f'{language}')
        button = self.get_button(buttons)
        print('click on button')
        # logger.info(f'{button} to click')
        time.sleep(2)
        self.click_on_button(button)
        # logger.info('Click on button to leave review')
        print('click on button')
        time.sleep(3)
        self.switch_to_iframe(self.driver, By.NAME, 'goog-reviews-write-widget')
        time.sleep(2)
        print('swith to frame')
        self.wait_element_for_click(self.driver, By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]')
        time.sleep(3)
        print('wait element for click')
        self.wait_element_for_click(self.driver, By.XPATH, '//*[@id="ZRGZAf"]/span')
        # logger.info('Review created')
        print('rewview created')

    def click_on_button(self, button):
        attempts = 20
        while attempts:
            try:
                button.click()
                return True
            except:
                attempts -= 1
                time.sleep(1)
        raise 'Cant click on button'
    def get_button(self,buttons):
        attempts = 20
        while attempts:
            try:
                for button in buttons:
                    review = button.get_attribute('data-value')
                    if review == '???????????????? ??????????':
                        time.sleep(1)
                        return button
                    elif review == 'Write a review':
                        time.sleep(1)
                        return button
            except:
                attempts -= 1
                time.sleep(1)
        raise 'No found required button'
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

    def close_context(self):
        self.driver.quit()

if __name__ == "__main__":
    try:
        obj = GoogleReviews()
        time.sleep(5)
        obj.get_page()
        time.sleep(5)
        obj.login()
        time.sleep(5)
        obj.get_review_page()
        time.sleep(5)
        obj.open_review()
        print('Account login 200')
        obj.close_context()
    except Exception as e:
        obj.close_context()
        print(f"{e}")
        print('vishla oshibka')
