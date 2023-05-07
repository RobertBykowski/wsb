import pytest

from pages.header_menu import HeaderMenu


# Use the "browser_setup" fixture from the conftest.py file
@pytest.mark.usefixtures("browser_setup")
class TestLogIn:
    # Test user login with correct credentials
    def test_user_login_with_correct_credentials(self):
        header_menu = HeaderMenu(self.driver, self.wait)
        # Open the login page by clicking on the login link in the header menu
        login_page = header_menu.open_login_page()
        # Enter the email and password
        login_page.write_email("tomasznowak@wp.pl")
        login_page.write_password("tomasznowak")
        # Click the login button
        login_page.click_login_button()
        # After successful login, the user should be redirected to the "My Account" page
        my_account_page = header_menu.open_my_account_page()
        # Check if the warning bar on the "My Account" page displays the correct text
        assert my_account_page.display_warning_bar() == "My account - Customer info"
        # Click the log out button to log out the user
        header_menu.click_log_out()

    # Test user login with incorrect credentials
    def test_user_login_with_incorrect_credentials(self):
        header_menu = HeaderMenu(self.driver, self.wait)
        # Open the login page
        login_page = header_menu.open_login_page()
        # Enter incorrect email and password
        login_page.write_email("adamwisniewski@wp.pl")
        login_page.write_password("adamwisniewski")
        # Click the login button
        login_page.click_login_button()
        # Check if the warning text on the login page displays the correct text
        assert login_page.display_warning_text() == "No customer account found"
