import pytest

from pages.header_menu import HeaderMenu


@pytest.mark.usefixtures("browser_setup")
class TestCart:

    # Test checking if the cart is empty when no items are added to it

    def test_no_item_in_cart(self):
        # Open the cart page and check if the info message is displayed
        header_menu = HeaderMenu(self.driver, self.wait)
        shopping_cart = header_menu.open_cart_page()
        assert shopping_cart.get_info_message() == "Your Shopping Cart is empty!"

    # Test checking if only one item is in the cart after adding one product to the cart

    def test_one_item_in_cart(self):
        product_name = "HTC One M8 Android L 5.0 Lollipop"

        # Search for the product and add it to the cart
        search_result_page = HeaderMenu(self.driver, self.wait).search_bar(product_name)
        product_page = search_result_page.click_product(product_name)
        quantity = product_page.write_quantity("1")
        product_page.add_to_cart()

        # Check if the actual quantity matches the expected quantity
        cart_page = HeaderMenu(self.driver, self.wait).open_cart_page()
        actual_quantity = cart_page.read_item('quantity')
        assert actual_quantity == quantity

        # Clean the cart after the test is complete
        cart_page.clean_cart()

    # Test checking if adding two items to the cart works correctly

    def test_two_items_in_cart(self):
        # Define the list of items to be added to the cart
        items = [
            {"name": "HTC One M8 Android L 5.0 Lollipop", "quantity": "1"},
            {"name": "Vintage Style Engagement Ring", "quantity": "1"}
        ]

        # Open the cart page
        header_menu = HeaderMenu(self.driver, self.wait)
        cart_page = header_menu.open_cart_page()

        # Add each item to the cart, and save the total quantity
        total_quantity = 0
        for item in items:
            search_result_page = header_menu.search_bar(item["name"])
            product_page = search_result_page.click_product(item["name"])
            quantity = product_page.write_quantity(item["quantity"])
            product_page.add_to_cart()
            total_quantity += int(quantity)

        # Check if the actual quantity matches the expected quantity
        actual_quantity = cart_page.read_item('quantity')
        assert actual_quantity == total_quantity

        # Clean the cart after the test is complete
        cart_page.clean_cart()

    # Test checking if the mechanism for updating the quantity of items in the cart is correct

    def test_quantity_update_in_cart(self):
        # Define the name of the product to be tested
        product_name = "HTC One M8 Android L 5.0 Lollipop"

        # Search for the product on the header menu
        search_result_page = HeaderMenu(self.driver, self.wait).search_bar(product_name)

        # Click on the product to navigate to the product page
        product_page = search_result_page.click_product(product_name)

        # Set the quantity of the product to 1 and add it to the cart
        product_page.write_quantity("1")
        product_page.add_to_cart()

        # Open the cart page
        header_menu = HeaderMenu(self.driver, self.wait)
        cart_page = header_menu.open_cart_page()

        # Update the quantity of the product to 2 and save the expected quantity
        quantity_update = "2"
        cart_page.update_quantity_value(quantity_update)
        expected_quantity = int(quantity_update)

        # Update the cart and save the actual quantity
        cart_page.update_cart()
        actual_quantity = cart_page.read_item('quantity')

        # Check if the actual quantity matches the expected quantity
        assert actual_quantity == expected_quantity

        # Clean the cart after the test is complete
        cart_page.clean_cart()
