#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.push_button_add_to_basket()
    page.solve_the_quiz()
    time.sleep(5)
    page.should_be_added_to_basket()
    time.sleep(5)
