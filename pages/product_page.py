#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def push_button_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def solve_the_quiz(self):
        self.solve_quiz_and_get_code()

    def should_be_added_to_basket(self):
        """ Проверка на совпадение имени и цены товара после добавления в корзину. """

        before_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        after_message = self.browser.find_element(*ProductPageLocators.MESSAGES).text
        assert before_name == after_message, f"Product did not add to the basket (product name {before_name} absents in the message {after_message})"

        before_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        after_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert before_price in after_price, "Product price does not corresponds to the basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
