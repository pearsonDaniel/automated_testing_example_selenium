# test_200_admin_modules.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_modules_page import AdminModulesPage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_admin_modules(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL + AdminModulesLocators.URL)
    admin_modules_page = AdminModulesPage(driver)
    admin_modules_page.verify_page_http_200_response(AdminModulesLocators.URL)
    print("###########################################################")