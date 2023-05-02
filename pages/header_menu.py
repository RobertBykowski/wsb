from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage
from pages.cart_page import CartPage
from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage


class HeaderMenu(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def open_register_page(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Register')]"))).click()
        register_page = RegisterPage(self.driver, self.wait)
        return register_page

    def open_cart_page(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Shopping cart')]"))).click()
        cart_page = CartPage(self.driver, self.wait)
        return cart_page

    def search_bar(self, product_name):
        box = self.wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        box.clear()
        box.send_keys(product_name)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(),'Search')]"))).click()
        search_result_page = SearchResultPage(self.driver, self.wait)
        return search_result_page
