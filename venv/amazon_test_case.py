import unittest
from amazon_page_locators import AmazonPageLocators
from amazon_page import AmazonPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMenu(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options, executable_path="./chromedriver")

    def tearDown(self):
        self.driver.close()


class TestAmazon(TestMenu):

    def setUp(self):
        super().setUp()
        self.home = AmazonPage(self.driver)

    def test_TC001(self):
        self.home.click(AmazonPageLocators.menu_button)
        self.home.click(AmazonPageLocators.electronics_button)
        self.home.click(AmazonPageLocators.cameras_button)


if __name__ == "__main__":
    unittest.main()
