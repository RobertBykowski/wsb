from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage

# Locators
INFO_MESSAGE = (By.XPATH, "//h1[contains(text(),'Search')]")


class SearchResultPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def get_info_message(self):
        return self.get_text(INFO_MESSAGE)

    def click_product(self, product_name):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name))).click()
        product_page = ProductPage(self.driver, self.wait)
        return product_page
