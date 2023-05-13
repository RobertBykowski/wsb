from selenium.webdriver.common.by import By

from pages.base_page import BasePage

email_box_loc = (By.XPATH, "//input[@id='Email']")
password_box_loc = (By.XPATH, "//input[@id='Password']")
log_in_button_loc = (By.XPATH, "//button[contains(text(),'Log in')]")
warning_text_loc = (By.XPATH, "//li[contains(text(),'No customer account found')]")


class LoginPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def write_email(self, email):
        self.fill_box(email_box_loc, email)

    def write_password(self, password):
        self.fill_box(password_box_loc, password)

    def click_login_button(self):
        self.click_button(log_in_button_loc)

    def display_warning_text(self):
        return self.get_text(warning_text_loc)


