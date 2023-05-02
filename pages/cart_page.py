from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
INFO_MESSAGE = (By.XPATH, "//div[contains(text(),'Your Shopping Cart is empty!')]")


class CartPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def get_info_message(self):
        return self.get_text(INFO_MESSAGE)

    def show_up_cart(self, item):
        cart_contents_list = self.get_cart_content()
        print(cart_contents_list[0][item])

