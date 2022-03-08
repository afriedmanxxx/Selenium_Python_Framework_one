from selenium.webdriver.common.by import By


class BasePageLocators():
        LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
        LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_URL = ()


class ProductPageLocators():
    ADD_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="row"]//p[@class="price_color"]')
    PRODUCT_NAME = (By.XPATH, '//article[@class="product_page"]//h1')
    VIEW_BASKET = (By.XPATH, '//span[@class="btn-group"]/a')
    BASKET_PRODUCT_PRICE = (By.XPATH, '//div[@class="basket-items"]//p[@class="price_color align-right"]')
    ITEM_ADDED_TO_BASKET = (By.XPATH, '//div[@class="basket-items"]//h3')
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")

