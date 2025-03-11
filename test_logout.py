# test_logout.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_logout():
        browsers = ["Chrome", "Edge", "Firefox"]
        for browser in browsers:
            driver = config_browser(browser)
            print(str(browser + " version: ") + str(driver.capabilities['browserVersion']))
            driver.get(Config.BASE_URL)
            time.sleep(3)
            login_page = LoginPage(driver)
            login_page.verify_page_http_200_response(LoginPageLocators.URL)
            login_page.login()
            time.sleep(2)
            login_page.verify_title()
            home_page = HomePage(driver)
            time.sleep(3)
            home_page.logout()
            print("###########################################################")
            # Close the WebDriver
            driver.quit()
