from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
   
# Create a browser object
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://demo.nopcommerce.com")
# Klinkni na Shopinng cart
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//li[@id='topcartlink']"))).click()
# Wyświetli się strona koszyka i kominikta "Your Shopping Cart is empty!"
notification = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Your Shopping Cart is empty!')]")))
print(notification.text)
time.sleep(4)

browser.quit()