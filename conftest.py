#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Set the language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nЗапуск браузера для теста...")

    language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    # Support only Chrome
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nЗавершение работы браузера...")
    browser.quit()  # Finish it!
