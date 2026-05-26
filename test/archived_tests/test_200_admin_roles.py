# test_200_admin_roles.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_roles_page import AdminRolesPage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_admin_roles(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL + AdminRolesLocators.URL)
    admin_roles_page = AdminRolesPage(driver)
    admin_roles_page.verify_page_http_200_response(AdminRolesLocators.URL)
    print("###########################################################")