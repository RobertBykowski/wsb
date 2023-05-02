from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Locators
FIELD_FIRSTNAME = (By.ID, "FirstName")
FIELD_LASTNAME = (By.ID, "LastName")
FIELD_EMAIL = (By.ID, "Email")
FIELD_PASSWORD = (By.ID, "Password")
FIELD_CONFIRMPASSWORD = (By.ID, "ConfirmPassword")
REGISTERBUTTON = (By.ID, "register-button")
CONFIRMATION_MESSAGE = (By.XPATH, "//div[contains(text(),'Your registration completed')]")
WARNINGMESSAGE = (By.XPATH, "//li[contains(text(),'The specified email already exists')]")


class RegisterPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # def get_title(self):
    #     message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Register')]")))
    #     return message.text

    def enter_register_details(self, firstname, lastname, email, password):
        self.fill_box(FIELD_FIRSTNAME, firstname)
        self.fill_box(FIELD_LASTNAME, lastname)
        self.fill_box(FIELD_EMAIL, email)
        self.fill_box(FIELD_PASSWORD, password)
        self.fill_box(FIELD_CONFIRMPASSWORD, password)

    def click_register_button(self):
        self.click_button(REGISTERBUTTON)

    def get_success_message(self):
        return self.get_text(CONFIRMATION_MESSAGE)

    def get_waring_message(self):
        return self.get_text(WARNINGMESSAGE)
