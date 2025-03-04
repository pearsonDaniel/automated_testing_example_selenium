# test_search_box.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_search_box():
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
            home_page = HomePage(driver)
            home_page.enter_search_term(BasePageLocators.SEARCH_TERM)
            time.sleep(3)
            home_page.verify_search_results(BasePageLocators.SEARCH_TERM)
            print("###########################################################")
            # Close the WebDriver
            driver.quit()
