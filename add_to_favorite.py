import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAddToFavorite(unittest.TestCase):
    FAVORITE_BUTTON = (By.XPATH, '//*[@id="my_wishlist"]')
    SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="masthead"]/div/div/div[2]/div/form/div[1]/div[2]/button[2]/i')
    PRODUS1 = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[2]/button[1]')
    PRODUS2 = (By.XPATH, '//*[@id="card_grid"]/div[2]/div/div/div[2]/button[1]')
    PRODUS3 = (By.XPATH, '//*[@id="card_grid"]/div[3]/div/div/div[2]/button[1]')
    FAVORITE_LIST = (By.XPATH, '//*[@id="main-container"]/section/div/div[2]/div/div/div[1]/div/span')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.emag.ro/')
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

    def test_add_more_then_one_product_to_favorite(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys('samsung')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        self.chrome.find_element(*self.PRODUS1).click()
        self.chrome.find_element(*self.PRODUS2).click()
        self.chrome.find_element(*self.PRODUS3).click()
        self.chrome.find_element(*self.FAVORITE_BUTTON).click()
        sleep(5)
        favorite_list_msg = self.chrome.find_element(*self.FAVORITE_LIST)
        print(favorite_list_msg.text)
