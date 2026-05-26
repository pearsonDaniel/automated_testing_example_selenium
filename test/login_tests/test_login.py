# test_login.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from locators.login_locators import LoginPageLocators
import time
import pytest
import requests


@pytest.mark.selenium
def test_login(config_browser):
        driver = config_browser
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        login_page.login()
        login_page.verify_title()
        print("###########################################################")