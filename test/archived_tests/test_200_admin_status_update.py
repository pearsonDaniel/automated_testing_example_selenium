# test_200_admin_status_update.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_status_update_page import AdminStatusUpdatePage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_admin_status_update(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL + AdminStatusUpdateLocators.URL)
    admin_status_update_page = AdminStatusUpdatePage(driver)
    admin_status_update_page.verify_page_http_200_response(AdminStatusUpdateLocators.URL)
    print("###########################################################")