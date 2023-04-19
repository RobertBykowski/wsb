from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_button (method, locator):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((method, locator))).click()

def fill_box(method, locator, str):
    box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((method, locator)))
    box.clear()
    box.send_keys(str)
    
# Create a browser object
browser = webdriver.Firefox()
browser.maximize_window()

browser.get("https://demo.nopcommerce.com")
email = "Ola@wp.pl"
password = "Ola"

click_button(By.XPATH,"//a[contains(text(),'Log in')]")
# Form for Returning Customer
fill_box(By.XPATH, "//input[@id='Email']", email)
fill_box(By.XPATH, "//input[@id='Password']", password)
click_button(By.XPATH,"//button[contains(text(),'Log in')]")
time.sleep(5)

browser.quit()