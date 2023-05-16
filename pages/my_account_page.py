# my_account_page.py

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# Locators
text_loc = (By.XPATH, "//h1[contains(text(),'My account - Customer info')]")


class MyAccountPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def display_warning_bar(self):
        return self.get_text(text_loc)
