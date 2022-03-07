from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, product_link)
    page.open()
    page.test_guest_can_add_product_to_basket()
