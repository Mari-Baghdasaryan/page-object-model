from selenium.webdriver.common.by import By


class AmazonPageLocators:
    menu_button = (By.ID, "nav-hamburger-menu")
    electronics_button = (By.XPATH, "//*[@id='hmenu-content']/ul[1]/li[7]/a")
    cameras_button = (By.XPATH, "//*[@id='hmenu-content']/ul[5]/li[4]/a")
