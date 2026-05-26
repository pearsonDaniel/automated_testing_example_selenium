# test_200_admin_rms.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_rms_page import AdminRMSPage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_admin_rms(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL + AdminRMSLocators.URL)
    admin_rms_page = AdminRMSPage(driver)
    admin_rms_page.verify_page_http_200_response(AdminRMSLocators.URL)
    print("###########################################################")