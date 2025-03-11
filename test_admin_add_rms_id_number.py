# test_admin_add_rms_id_number.py
from conftest import Config
from conftest import config_browser
from src.pages.login_page import LoginPage
from src.pages.admin_rms_page import AdminRMSPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_add_rms_id_number(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.verify_title()
    time.sleep(2)
    login_page.login()
    driver.get(Config.BASE_URL+AdminRMSLocators.URL)
    admin_rms_page = AdminRMSPage(driver)
    admin_rms_page.verify_page_http_200_response(AdminRMSLocators.URL)
    time.sleep(3)
    print("###########################################################")
    driver.quit()
