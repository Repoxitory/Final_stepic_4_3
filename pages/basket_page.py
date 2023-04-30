#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        """ Проверка на пустоту корзины. """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket should be empty bu it is not..."

    def should_be_text_of_empty_basket(self):
        """ Проверка, что есть текст о пустоте корзины. """
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "The basket message does not exist, but it should be"
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text, "The basket message does not exist, but it should be"
