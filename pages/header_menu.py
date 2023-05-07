from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.cart_page import CartPage

# Importing necessary page classes
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.register_page import RegisterPage
from pages.search_result_page import SearchResultPage


class HeaderMenu(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver
        self.wait = wait

    # Locators
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Register')]")
    SHOPPING_CART_LINK = (By.XPATH, "//span[contains(text(),'Shopping cart')]")
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, ".//button[contains(text(),'Search')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Log in')]")
    MY_ACCOUNT_LINK = (By.XPATH, "//a[@class='ico-account'][text()='My account']")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Log out')]")

    def open_register_page(self):
        self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK)).click()
        register_page = RegisterPage(self.driver, self.wait)
        return register_page

    def open_cart_page(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_LINK)).click()
        cart_page = CartPage(self.driver, self.wait)
        return cart_page

    def search_bar(self, product_name):
        box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        box.clear()
        box.send_keys(product_name)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        search_result_page = SearchResultPage(self.driver, self.wait)
        return search_result_page

    def open_login_page(self):
        menu = self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK))
        menu.click()
        login_page = LoginPage(self.driver, self.wait)
        return login_page

    def open_my_account_page(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT_LINK)).click()
        my_account_page = MyAccountPage(self.driver, self.wait)
        return my_account_page

    def click_log_out(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()
