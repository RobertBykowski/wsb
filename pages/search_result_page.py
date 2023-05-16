# search_result_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.product_page import ProductPage

# Locators
text_loc = (By.XPATH, "//div[contains(text(),'No products were found that matched your criteria.')]")
product_links_loc = (
    By.XPATH, "//div[@class='products-container']//div[@class='product-item']//h2[@class='product-title']/a")


class SearchResultPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def display_info_text(self):
        return self.get_text(text_loc)

    def click_product(self, product_name):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, product_name))).click()
        product_page = ProductPage(self.driver, self.wait)
        return product_page

    def get_search_result(self):
        elements = self.driver.find_elements(*product_links_loc)
        search_results = []
        for element in elements:
            search_results.append(element.text)
        return search_results
