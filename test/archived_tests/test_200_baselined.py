# test_200_baselined.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.baselined_co_mod_required_page import BaselinedCOMODRequiredPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_200_baselined(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL+BaselinedCOMODRequiredLocators.URL)
    baselined_co_mod_required_page = BaselinedCOMODRequiredPage(driver)
    baselined_co_mod_required_page.verify_page_http_200_response(BaselinedCOMODRequiredLocators.URL)
    print("###########################################################")