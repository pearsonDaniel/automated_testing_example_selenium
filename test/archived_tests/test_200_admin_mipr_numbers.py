# test_200_admin_mipr_numbers.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_numbers_page import AdminMiprPage
from locators.locators import *
import pytest
import time


@pytest.mark.selenium
def test_200_admin_mipr_numbers(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL + AdminMiprNumberLocators.URL)
    admin_mipr_page = AdminMiprPage(driver)
    admin_mipr_page.verify_page_http_200_response(AdminMiprNumberLocators.URL)
    print("###########################################################")