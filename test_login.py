# test_login.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_login():

        browsers = ["Chrome", "Edge", "Firefox"]

        for browser in browsers:
                driver = config_browser(browser)
                driver.get(Config.BASE_URL)
                time.sleep(3)
                login_page = LoginPage(driver)
                login_page.verify_page_http_200_response(LoginPageLocators.URL)
                login_page.login()
                time.sleep(2)
                login_page.verify_title()
                print("###########################################################")
                # Close the WebDriver
                driver.quit()
