from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# Locators
text_loc = (By.XPATH, "//div[contains(text(),'Your Shopping Cart is empty!')]")
qty_box_loc = (By.XPATH, "//input[@class='qty-input']")
button_update_shopping_cart_loc = (By.XPATH, "//button[@id='updatecart']")


class CartPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def get_info_message(self):
        return self.get_text(text_loc)

    def read_item(self, key):
        cart_contents_list = self.get_cart_content()
        total_quantity = 0
        for item in cart_contents_list:
            total_quantity += int(item[key])
        return total_quantity

    def update_quantity_value(self, qty):
        self.fill_box(qty_box_loc, qty)

    def update_cart(self):
        self.click_button(button_update_shopping_cart_loc)
