# test_logout.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_logout(request):
        browser = request.config.getoption("--browser")
        driver = config_browser(browser)
        print(str(browser + " version: ") + str(driver.capabilities['browserVersion']))
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        login_page.login()
        login_page.verify_title()
        home_page = HomePage(driver)
        home_page.logout()
        print("###########################################################")
        driver.quit()
