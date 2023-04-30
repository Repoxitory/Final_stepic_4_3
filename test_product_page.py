#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import time

from .pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    """
        1. Открываем страницу товара
        2. Нажимаем на кнопку "Добавить в корзину".
        3. Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code()

        Ожидаемый результат:
        1. Cообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать товаром, который добавили.
        2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    """

    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.push_button_add_to_basket()
    page.solve_the_quiz()
    time.sleep(1)
    page.should_be_added_to_basket()
    time.sleep(1)
    # page.success_message_should_disappear()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """

    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.push_button_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
        1. Открываем страницу товара
        2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """

    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
        1. Открываем страницу товара
        2. Добавляем товар в корзину
        3. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """

    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.push_button_add_to_basket()
    page.success_message_should_disappear()