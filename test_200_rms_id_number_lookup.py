# test_200_rms_id_number_lookup.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.rms_id_number_lookup_page import RmsIdNumberLookupPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_200_rms_id_number_lookup(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL+RmsIdNumberLookupLocators.URL)
    rms_id_number_lookup_page = RmsIdNumberLookupPage(driver)
    rms_id_number_lookup_page.verify_page_http_200_response(RmsIdNumberLookupLocators.URL)
    print("###########################################################")