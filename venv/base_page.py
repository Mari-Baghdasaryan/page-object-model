
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, by_locator, string_text):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(string_text)

    def click(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def clear(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        element.clear()

    def select(self, by_locator, visible_text):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        Select(element).select_by_visible_text(visible_text)

    def move_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_element_text(self, by_locator, element_text):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        assert element.text == element_text

    def assert_validation_message(self, by_locator, element_text):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        assert element.get_attribute("validationMessage") == element_text

    def click_on_rnd_element(self, by_locator):
        import random
        elements = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(by_locator))
        element = random.choice(elements)
        element.click()
