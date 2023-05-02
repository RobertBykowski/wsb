import pytest
from pages.header_menu import HeaderMenu
# from utilities.utils import Utils


@pytest.mark.usefixtures("browser_setup")
class TestRegisterPage:

    # def generate_personal_data(self):
    #     ut = Utils()
    #     firstname = ut.generate_name()
    #     lastname = ut.generate_lastname()
    #     email = ut.generate_email()
    #     password = ut.generate_password()
    #     return firstname, lastname, email, password

    def test_pos_register_new_user(self):
        # firstname, lastname, email, password = self.generate_personal_data()

        rp = HeaderMenu(self.driver, self.wait)
        register_page = rp.open_register_page()
        # register_page.enter_register_details(firstname, lastname, email, password)
        register_page.enter_register_details("Adam", "Nowak", "adamnowak@wp.pl", "tomasznowak")
        register_page.click_register_button()
        assert register_page.get_success_message() == "Your registration completed"

    def test_neg_register_new_user(self):
        # firstname, lastname, email, password = self.generate_personal_data()
        rp = HeaderMenu(self.driver, self.wait)
        register_page = rp.open_register_page()
        # register_page.enter_register_details(firstname, lastname, email, password)
        register_page.enter_register_details("Tomasz", "Nowak", "tomasznowak@wp.pl", "tomasznowak")
        register_page.click_register_button()
        assert register_page.get_waring_message() == "The specified email already exists"
