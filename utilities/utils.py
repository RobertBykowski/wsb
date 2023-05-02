import random


class Utils:

    def __init__(self):
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
