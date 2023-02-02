import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestHomePage(unittest.TestCase):
    LOGO_BUTTON = (By.XPATH, '//*[@id="masthead"]/div/div/div[1]/a/img')
    SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="masthead"]/div/div/div[2]/div/form/div[1]/div[2]/button[2]/i')
    INTERACTIVE_MESSAGE = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/img')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="main-container"]/section/div/div[3]/h1/span[1]')
    ANPC_BUTTON = (By.XPATH, '/html/body/div[4]/footer/div[3]/div/div/div[3]/span[3]/a[1]')
    LISTA_OPTIUNI = (By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/ul')
    CONTUL_MEU_BUTTON = (By.XPATH, '//*[@id="my_account"]')
    FAVORITE_BUTTON = (By.XPATH, '//*[@id="my_wishlist"]')
    COSUL_MEU_BUTTON = (By.XPATH, '//*[@id="my_cart"]')
    chrome = None

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.emag.ro/')
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        self.chrome.quit()

    def test_url(self) -> None:
        actual = self.chrome.current_url
        expected = 'https://www.emag.ro/'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_logo(self):
        elem = self.chrome.find_element(*self.LOGO_BUTTON)
        self.assertTrue(elem.is_displayed(), 'Logo-ul nu e vizibil')

    def test_search_box_input(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys('Telefon')

    def test_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def test_interactive_message_is_displayed(self):
        elem = self.chrome.find_element(*self.INTERACTIVE_MESSAGE)
        self.assertTrue(elem.is_displayed(), 'Mesajul nu e vizibil')

    def test_error_message_for_no_results(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys('sdjdkfhacydwiqmcnfqfyeru')
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        elem = self.chrome.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(elem.is_displayed(), 'Mesajul nu e vizibil')

    def test_anpc_button_is_enable(self):
        elem = self.chrome.find_element(*self.ANPC_BUTTON)
        self.assertTrue(elem.is_enabled(), 'Butonul nu este activ')

    def test_active_element(self):
        elem = self.chrome.switch_to.active_element
        self.assertTrue(elem.is_displayed(), 'Elementele nu sunt active')

    def test_active_element_click(self):
        self.chrome.switch_to.active_element.click()

    def test_menu_options(self):
        self.meniu = self.chrome.find_element(*self.LISTA_OPTIUNI)
        self.meniu.click()
        self.optiuni = self.meniu.text
        self.assertTrue(len(self.optiuni) > 0, 'Nu sunt prezente optiuni in meniu')
        print(self.optiuni)

    def test_contul_meu_button(self):
        self.chrome.find_element(*self.CONTUL_MEU_BUTTON).click()

    def test_favorite_button(self):
        self.chrome.find_element(*self.FAVORITE_BUTTON).click()

    def test_cosul_meu_button(self):
        self.chrome.find_element(*self.COSUL_MEU_BUTTON).click()







