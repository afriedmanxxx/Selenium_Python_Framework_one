from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        self.add_to_basket()
        self.check_product_added_to_basket()
        self.check_basket_price_equal_product_price()

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def check_product_added_to_basket(self):
        check_basket = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        check_basket.click()

    def check_basket_price_equal_product_price(self):
        item_added_to_basket = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET)
        assert item_added_to_basket != None, "Item is not added to basket"
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE)
        assert len(basket_product_price.text) > 2, "Price is not shown"



