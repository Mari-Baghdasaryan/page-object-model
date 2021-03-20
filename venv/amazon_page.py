from base_page import BasePage


class AmazonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://amazon.com")