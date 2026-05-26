# test_200_admin_tabs.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_tabs_page import AdminTabsPage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_admin_tabs(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(5)
    driver.get(Config.BASE_URL + AdminTabsLocators.URL)
    admin_tabs_page = AdminTabsPage(driver)
    admin_tabs_page.verify_page_http_200_response(AdminTabsLocators.URL)
    print("###########################################################")