#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """ Проверка на корректный url адрес. """
        assert "login" in self.browser.current_url, "Login URL-link is correct"

    def should_be_login_form(self):
        """ Проверка, что есть форма логина. """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """ Проверка, что есть форма регистрации на странице. """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
