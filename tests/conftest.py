# Ogólnie rzecz biorąc, ten kod przygotowuje środowisko testowe (przeglądarkę internetową)
# i czeka na zakończenie testów, aby móc je posprzątać.

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

URL = "https://demo.nopcommerce.com"
"""
@pytest.fixture(scope="class") to dekorator, który tworzy funkcję setup 
i definiuje jej zasięg class, co oznacza, że ta funkcja będzie wywoływana 
tylko raz dla każdej klasy testowej."""


@pytest.fixture(scope="class")
def browser_setup(request):
    # Create a browser object
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)
    driver.get(URL)
    driver.delete_all_cookies()
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.quit()
