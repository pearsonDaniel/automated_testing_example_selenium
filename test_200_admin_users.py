# test_200_admin_users.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_users_page import AdminUsersPage
from locators.locators import *
import pytest


@pytest.mark.selenium
def test_200_admin_users(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL + AdminUsersLocators.URL)
    admin_users_page = AdminUsersPage(driver)
    admin_users_page.verify_page_http_200_response(AdminUsersLocators.URL)
    print("###########################################################")