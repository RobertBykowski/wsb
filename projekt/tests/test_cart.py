import pytest
from pages.launch_product_page import LaunchProductPage

product_name = "adidas Consortium Campus 80s Running Shoes"
product_qty = 5


@pytest.mark.usefixtures("setup")
class TestCart():

    def test_add__product_to_cart(self):
        lp = LaunchProductPage(self.driver, self.wait)
        lp.add_product_to_cart(product_name, product_qty)
        expected_cart_qty = product_qty
        actual_cart_qty = lp.get_cart()
        assert int(actual_cart_qty) == expected_cart_qty
        

    

       
     

     

   
    