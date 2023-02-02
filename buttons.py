import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Buttons(unittest.TestCase):
    INPUT_EMAIL = (By.XPATH, '//*[@id="user_login_email"]')
    CONTINUA_BUTTON = (By.XPATH, '//*[@id="user_login_continue"]')
    MESSAGE = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]')
    FACEBOOK_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/a[1]')
    GOOGLE_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/a[2]')
    APPLE_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/a[3]')
    AJUTOR_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/a')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://auth.emag.ro/user/login')
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

    def test_url(self) -> None:
        actual = self.chrome.current_url
        expected = 'https://auth.emag.ro/user/login'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_input_mail(self):
        self.chrome.find_element(*self.INPUT_EMAIL).send_keys('email@gmail.com')

    def test_continua_button(self):
        self.chrome.find_element(*self.CONTINUA_BUTTON).click()

    def test_message(self):
        elem = self.chrome.find_element(*self.MESSAGE)
        self.assertTrue(elem.is_displayed(), 'Mesajul nu este afisat')

    def test_buttons(self):
        self.chrome.find_element(*self.FACEBOOK_BUTTON).click()
        self.chrome.back()
        self.chrome.find_element(*self.GOOGLE_BUTTON).click()
        self.chrome.back()
        self.chrome.find_element(*self.APPLE_BUTTON).click()
        self.chrome.back()
        self.chrome.find_element(*self.AJUTOR_BUTTON).click()
        self.chrome.back()




