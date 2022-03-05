from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        link = self.url
        assert "login" in link, "Not correct URL link observed."

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"