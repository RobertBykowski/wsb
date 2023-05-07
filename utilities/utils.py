import random
from pages.base_page import BasePage
from pages.header_menu import HeaderMenu
from pages.register_page import RegisterPage

class Utils(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

        self.imiona = [
            "Adam",
            "Barbara",
            "Cezary",
            "Dorota",
            "Ewa",
            "Filip",
            "Gabriela",
            "Hanna",
            "Igor",
        ]
        self.nazwiska = [
            "Kowalski",
            "Nowak",
            "Wiśniewski",
            "Dąbrowski",
            "Lewandowski",
            "Wójcik",
            "Kamiński",
            "Kowalczyk",
            "Zieliński",
            "Szymański",
            "Woźniak",
            "Kozłowski",
            "Jankowski",
            "Mazur",
            "Kwiatkowski",
            "Kaczmarek",
            "Piotrowski",
            "Grabowski",
            "Nowakowski",
            "Pawłowski",
        ]

    def generate_name(self):
        return random.choice(self.imiona)

    def generate_lastname(self):
        return random.choice(self.nazwiska)

    def generate_email(self):
        firstname = self.generate_name()
        lastname = self.generate_lastname()
        email = firstname + lastname + "@wp.pl"
        return email.lower()

    def generate_password(self):
        firstname = self.generate_name()
        lastname = self.generate_lastname()
        password = firstname + lastname.lower()
        return password

    def create_new_user_on_database(self):
        header_menu = HeaderMenu(self.driver, self.wait)
        register_page = header_menu.open_register_page()
        # Enter valid registration details
        name = self.generate_name()
        lastname = self.generate_lastname()
        email = self.generate_email()
        password = self.generate_password()
        register_page.enter_register_details(name, lastname, email, password)
        register_page.click_register_button()
        return email, password

