# test_admin_portal.py
from conftest import Config
from conftest import config_browser
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.admin_portal_page import AdminPortalPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_admin_portal(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    home_page = HomePage(driver)
    home_page.click_admin_portal()
    admin_portal_page = AdminPortalPage(driver)
    admin_portal_page.verify_page_http_200_response(AdminPortalPageLocators.URL)
    print("###########################################################")