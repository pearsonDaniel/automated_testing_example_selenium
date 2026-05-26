# test_base_search.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_base_search(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    time.sleep(2)
    login_page.login()
    home_page = HomePage(driver)
    time.sleep(5)
    home_page.enter_search_term("DJP")
    time.sleep(5)
    print("###########################################################")