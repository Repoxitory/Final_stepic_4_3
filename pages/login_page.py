#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators


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

    def register_new_user(self, email, password):
        """ Регистрация нового пользователя. """

        email = str(time.time()) + "@fakemail.org"
        password = "password1234567890"

        self.browser.get(self.url)
        self.browser.find_element(*RegisterPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.PASSWORD1).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.PASSWORD2).send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
