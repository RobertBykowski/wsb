import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# Locators
product_quantity_loc = (By.CSS_SELECTOR, "input.qty-input")
add_to_cart_loc = (By.XPATH, ".//button[contains(text(), 'Add to cart')]")
warning_text_loc = (By.XPATH, "//p[contains(text(),'Quantity should be positive')]")


class ProductPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def write_quantity(self, qty):
        self.fill_box(product_quantity_loc, qty)
        return int(qty)

    def add_to_cart(self):
        self.click_button(add_to_cart_loc)
        time.sleep(5)

    def display_warning_bar(self):
        return self.get_text(warning_text_loc)
