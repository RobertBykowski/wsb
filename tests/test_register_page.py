import pytest
from pages.header_menu import HeaderMenu


# Use the "browser_setup" fixture from the conftest.py file
@pytest.mark.usefixtures("browser_setup")
class TestRegisterPage:

    # Positive test for registering a new user
    def test_pos_register_new_user(self):
        header_menu = HeaderMenu(self.driver, self.wait)
        register_page = header_menu.open_register_page()
        # Enter valid registration details
        register_page.enter_register_details("Adam", "Nowak", "adamnowak@wp.pl", "tomasznowak")
        register_page.click_register_button()
        # Check if success message is displayed
        assert register_page.get_success_message() == "Your registration completed"

    # Negative test for registering a new user with already existing email
    def test_neg_register_new_user(self):
        header_menu = HeaderMenu(self.driver, self.wait)
        register_page = header_menu.open_register_page()
        # Enter registration details with already existing email
        register_page.enter_register_details("Tomasz", "Nowak", "tomasznowak@wp.pl", "tomasznowak")
        register_page.click_register_button()
        # Check if warning message is displayed
        assert register_page.get_warning_message() == "The specified email already exists"
