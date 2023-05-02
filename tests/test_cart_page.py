import time

import pytest
from pages.header_menu import HeaderMenu


@pytest.mark.usefixtures("browser_setup")
class TestCart:
    # Test sprawdzający, czy koszyk jest pusty, gdy nie dodano żadnych produktów;
    # def test_no_item_in_cart(self):
    #     sc = HeaderMenu(self.driver, self.wait)
    #     shopping_cart = sc.open_cart_page()
    #     assert shopping_cart.get_info_message() == "Your Shopping Cart is empty!"

    # Test sprawdzający, czy po dodaniu jednego produktu do koszyka, w koszyku znajduje się tylko jeden produkt;
    def test_one_item_in_cart(self):
        product_name = "HTC One M8 Android L 5.0 Lollipop"

        sb = HeaderMenu(self.driver, self.wait)
        search_result_page = sb.search_bar(product_name)
        product_page = search_result_page.click_product(product_name)
        product_page.write_quantity("1")
        product_page.add_to_cart()
        time.sleep(5)
        cp = HeaderMenu(self.driver, self.wait)
        cart = cp.open_cart_page()
        cart.show_up_cart('product')
        # sprawdź ilość produktów w koszyku

