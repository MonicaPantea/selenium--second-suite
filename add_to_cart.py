import unittest
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestAddToCart(unittest.TestCase):
    CART_BUTTON = (By.XPATH, '//*[@id="my_cart"]')
    SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="masthead"]/div/div/div[2]/div/form/div[1]/div[2]/button[2]/i')
    PRODUCT1 = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[4]/div[2]/form/button')
    PRODUCT2 = (By.XPATH, '//*[@id="card_grid"]/div[2]/div/div/div[4]/div[2]/form/button')
    PRODUCT3 = (By.XPATH, '//*[@id="card_grid"]/div[3]/div/div/div[4]/div[2]/form/button')
    CART_SUMARY = (By.XPATH, '//*[@id="main-container"]/section/div/div[2]/div/div/div[1]/div/span')
    CLOSE_WINDOW = (By.CLASS_NAME, 'em em-close gtm_6046yfqs')
    POPUP_WINDOW = (By.XPATH, '/html/body/div[12]/div')
    POPUP_CLOSE_WINDOW_BUTTON = (By.CLASS_NAME, '/html/body/div[12]/div/div/div[1]/button/i')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.emag.ro/')
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

    # DE VAZUT CUM SE INCHIDE FEREASTRA POPUP

    def test_add_to_cart(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys('samsung')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUCT1).click()
        iframe = self.chrome.find_elements(By.TAG_NAME, 'iframe[7]')
        self.chrome.switch_to.frame(iframe)
        self.chrome.find_element(*self.POPUP_CLOSE_WINDOW_BUTTON).click()
        sleep(5)
        self.chrome.find_element(*self.CLOSE_WINDOW).click()
        sleep(5)
        self.chrome.find_element(*self.PRODUCT2).click()
        sleep(5)
        self.chrome.find_element(*self.PRODUCT3).click()
        sleep(5)
        self.chrome.find_element(*self.CART_BUTTON).click()
        sleep(5)
        cart_sumary = self.chrome.find_element(*self.CART_SUMARY)
        print(cart_sumary.text)


