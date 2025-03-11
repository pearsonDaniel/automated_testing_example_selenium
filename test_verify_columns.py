# test_verify_columns.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_verify_columns(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()
    time.sleep(5)
    home_page = HomePage(driver)
    home_page.click_columns_toggle("Manage Columns")
    home_page.verify_column_options()
    print("###########################################################")
    driver.quit()
