# test_200_financial_management.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_200_financial_management(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    home_page = HomePage(driver)
    home_page.verify_page_http_200_response(Config.BASE_URL+HomePageLocators.URL)
    print("###########################################################")