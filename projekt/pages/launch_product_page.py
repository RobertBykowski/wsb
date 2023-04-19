from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LaunchProductPage():
    def __init__(self, driver, wait):
        # super().__init__(driver)
        self.driver = driver
        self.wait = wait


    def add_product_to_cart(self, product_name, product_quantity):
        # Wyszukanie produktu, który zostanie dodany do koszyka
        box = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='small-searchterms']")))
        box.send_keys(product_name)
        box.send_keys(Keys.ENTER)
        
        # Przejście na stronę produktu 
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//body/div[6]/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/h2[1]/a[1]"))).click()
        dropdown_trigger = self.driver.find_element(By.ID,'product_attribute_9')
        dropdown_trigger.click()
        dropdown = self.wait.until(EC.presence_of_element_located((By.ID, 'product_attribute_9')))
        first_dropdown_item = dropdown.find_element(By.XPATH,"//option[contains(text(),'8')]")
        first_dropdown_item.click()
        # Podanie ilości produktu 
        box_qty = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#product_enteredQuantity_25")))
        box_qty.clear()
        box_qty.send_keys(product_quantity)
        # Kliknięcie przycisku "Add to Cart"
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-button-25']"))).click()
        time.sleep(5)    

        # Przejście do koszyka i pobranie ilości produktu
    def get_cart(self):
        
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Shopping cart')]"))).click()
        
        qty_product = self.wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div[2]/div/form/div[1]/table/tbody/tr/td[5]/input")))
        
        value = qty_product.get_attribute("value")
        time.sleep(5)
        return value

        
        