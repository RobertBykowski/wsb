from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
product_quantity = (By.CSS_SELECTOR, "input.qty-input")
add_to_cart = (By.XPATH, ".//button[contains(text(), 'Add to cart')]")


class ProductPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def write_quantity(self, qty):
        self.fill_box(product_quantity, qty)

    def add_to_cart(self):
        self.click_button(add_to_cart)

