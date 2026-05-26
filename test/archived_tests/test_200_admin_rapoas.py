# test_200_admin_rapoas.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_rapoas_page import AdminRAPOAsPage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_admin_rapoas(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL + AdminRAPOAsLocators.URL)
    admin_rapoas_page = AdminRAPOAsPage(driver)
    admin_rapoas_page.verify_page_http_200_response(AdminRAPOAsLocators.URL)
    print("###########################################################")