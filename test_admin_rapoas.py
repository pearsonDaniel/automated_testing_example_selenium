# test_admin_rapoas.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_rapoas_page import AdminRAPOAsPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_admin_rapoas(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    time.sleep(2)
    login_page.login()
    login_page.verify_title()
    driver.get(Config.BASE_URL + AdminRAPOAsLocators.URL)
    admin_rapoas_page = AdminRAPOAsPage(driver)
    admin_rapoas_page.verify_page_http_200_response(AdminRAPOAsLocators.URL)
    print("###########################################################")
    driver.quit()
