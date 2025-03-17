# test_login.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from locators.locators import *
import time
import pytest
import requests


@pytest.mark.selenium
def test_login(request):
        browser = request.config.getoption("--browser")
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        login_page.login()
        login_page.verify_title()
        print("###########################################################")
        driver.quit()
