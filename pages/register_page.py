from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # Locators
    field_firstname_loc = (By.ID, "FirstName")
    field_lastname_loc = (By.ID, "LastName")
    field_email_loc = (By.ID, "Email")
    field_password_loc = (By.ID, "Password")
    field_confirmpassword_loc = (By.ID, "ConfirmPassword")
    registerbutton_loc = (By.ID, "register-button")
    confirmation_message_loc = (By.XPATH, "//div[contains(text(),'Your registration completed')]")
    warningmessage_loc = (By.XPATH, "//li[contains(text(),'The specified email already exists')]")

    def enter_register_details(self, firstname, lastname, email, password):
        self.fill_box(self.field_firstname_loc, firstname)
        self.fill_box(self.field_lastname_loc, lastname)
        self.fill_box(self.field_email_loc, email)
        self.fill_box(self.field_password_loc, password)
        self.fill_box(self.field_confirmpassword_loc, password)

    def click_register_button(self):
        self.click_button(self.registerbutton_loc)

    def get_success_message(self):
        return self.get_text(self.confirmation_message_loc)

    def get_warning_message(self):
        return self.get_text(self.warningmessage_loc)
