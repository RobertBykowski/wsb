# test_product_finder.py

import pytest

# importing the HeaderMenu class from the pages.header_menu module
from pages.header_menu import HeaderMenu
# loading test data from the test_data.json file
from utilities.utils import get_test_data


# Use the "browser_setup" fixture from the conftest.py file


@pytest.mark.usefixtures("browser_setup")
class TestProductFinder:

    # testing the search for an existing product with given the name of product or keywords
    @pytest.mark.parametrize("keyword", ["Apple", "Nike", "apple", "nike"])
    def test_positive_product_search(self, keyword):
        # searching for the product using the keyword in the search bar
        search_result_page = HeaderMenu(self.driver, self.wait).search_bar(keyword)
        # getting the search results
        search_results = search_result_page.get_search_result()
        # asserting that at least one result contains the given keyword
        assert any(keyword.lower() in result.lower() for result in
                   search_results)

    # testing the search for a nonexistent product with the keywords from the test_data.json file

    @pytest.mark.parametrize("keyword", [data["keyword"] for data in get_test_data()])
    # @pytest.mark.parametrize("keyword", [data["keyword"] for data in test_data])
    def test_search_for_nonexistent_product(self, keyword):
        # searching for the product using the keyword in the search bar
        search_result_page = HeaderMenu(self.driver, self.wait).search_bar(keyword)
        # getting the info text displayed on the search results page
        search_results = search_result_page.display_info_text()
        # asserting that the displayed text matches the expected text for nonexistent products
        assert search_results == "No products were found that matched your criteria."
