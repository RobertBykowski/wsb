import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators
    product_quantity_loc = (By.CSS_SELECTOR, "input.qty-input")
    add_to_cart_loc = (By.XPATH, ".//button[contains(text(), 'Add to cart')]")
    warning_text_loc = (By.XPATH, "//p[contains(text(),'Quantity should be positive')]")

    def write_quantity(self, qty):
        self.fill_box(self.product_quantity_loc, qty)
        return int(qty)

    def add_to_cart(self):
        self.click_button(self.add_to_cart_loc)
        time.sleep(5)

    def display_warning_bar(self):
        return self.get_text(self.warning_text_loc)
