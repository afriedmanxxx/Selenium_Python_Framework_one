from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        product_name = self.get_product_name()
        price = self.get_product_price()
        #self.should_not_be_success_message()
        self.add_to_basket()
        time.sleep(3)
        self.check_product_added_to_basket()
        self.check_basket_price_equal_product_price(price=price, product_name=product_name)

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        time.sleep(1)

    def check_product_added_to_basket(self):
        check_basket = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        check_basket.click()

    def check_basket_price_equal_product_price(self, price, product_name):
        item_added_to_basket = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET)
        assert item_added_to_basket.text == product_name, "Item is not added to basket"
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE)
        assert basket_product_price.text == price, "Price is wrong"

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"




