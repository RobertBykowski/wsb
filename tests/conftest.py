# conftest.py

import os
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

URL = "https://demo.nopcommerce.com"
"""
The @pytest.fixture(scope="class") is a decorator that creates a setup function
and defines its scope as "class," which means that this function will be called
only once for each test class."""


@pytest.fixture(scope="class")
def browser_setup(request, browser):
    # Create a browser object
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

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


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

