# header_menu.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.register_page import RegisterPage
from pages.search_result_page import SearchResultPage

# Locators
register_link_loc = (By.XPATH, "//a[contains(text(),'Register')]")
shopping_cart_link_loc = (By.XPATH, "//span[contains(text(),'Shopping cart')]")
search_box_loc = (By.ID, "small-searchterms")
search_button_loc = (By.XPATH, ".//button[contains(text(),'Search')]")
login_link_loc = (By.XPATH, "//a[contains(text(),'Log in')]")
my_account_link_loc = (By.XPATH, "//a[@class='ico-account'][text()='My account']")
logout_link_loc = (By.XPATH, "//a[contains(text(),'Log out')]")


class HeaderMenu(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    def open_register_page(self):
        self.wait.until(EC.element_to_be_clickable(register_link_loc)).click()
        register_page = RegisterPage(self.driver, self.wait)
        return register_page

    def open_cart_page(self):
        self.wait.until(EC.element_to_be_clickable(shopping_cart_link_loc)).click()
        cart_page = CartPage(self.driver, self.wait)
        return cart_page

    def search_bar(self, product_name):
        box = self.wait.until(EC.element_to_be_clickable(search_box_loc))
        box.clear()
        box.send_keys(product_name)
        self.wait.until(EC.element_to_be_clickable(search_button_loc)).click()
        search_result_page = SearchResultPage(self.driver, self.wait)
        return search_result_page

    def open_login_page(self):
        menu = self.wait.until(EC.visibility_of_element_located(login_link_loc))
        menu.click()
        login_page = LoginPage(self.driver, self.wait)
        return login_page

    def open_my_account_page(self):
        self.wait.until(EC.element_to_be_clickable(my_account_link_loc)).click()
        my_account_page = MyAccountPage(self.driver, self.wait)
        return my_account_page

    def click_log_out(self):
        self.wait.until(EC.element_to_be_clickable(logout_link_loc)).click()
