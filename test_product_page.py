#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
        1. Гость открывает страницу товара
        2. Переходит в корзину по кнопке в шапке
        3. Ожидаем, что в корзине нет товаров
        4. Ожидаем, что есть текст о том что корзина пуста
    """

    url = "http://selenium1py.pythonanywhere.com/ru/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_of_empty_basket()
