from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestAddProcuctToCart():

    def test_add__product_to_cart(self):
    
        browser = webdriver.Firefox() # Create a browser object
        browser.delete_all_cookies()
        browser.maximize_window()
        browser.get("https://demo.nopcommerce.com")
        box = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='small-searchterms']")))
        box.send_keys("adidas Consortium Campus 80s Running Shoes")
        box.send_keys(Keys.ENTER)
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((
            By.XPATH,"//body/div[6]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]/a[1]"))).click()

        dropdown_trigger = browser.find_element(By.ID,'product_attribute_9')
        dropdown_trigger.click()
        dropdown = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'product_attribute_9'))
            )

        first_dropdown_item = dropdown.find_element(By.XPATH,"//option[contains(text(),'8')]")
        first_dropdown_item.click()
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((
            By.XPATH,"//button[@id='add-to-cart-button-25']"))).click()
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((
            By.XPATH,"//body/div[@id='bar-notification']/div[1]/span[1]"))).click()

        time.sleep(2)
        WebDriverWait(browser,20).until(EC.element_to_be_clickable((
            By.XPATH,"//span[contains(text(),'Shopping cart')]"))).click()

        element = WebDriverWait(browser,20).until(EC.element_to_be_clickable((
            By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/div/form/div[1]/table/tbody/tr/td[5]/input")))

        value = element.get_attribute("value")
        print(value)

        browser.quit()

tc = TestAddProcuctToCart()
tc.test_add__product_to_cart()
    