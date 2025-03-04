# test_dropdown_menu.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_dropdown_menu():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        login_page.login()
        time.sleep(5)
        home_page = HomePage(driver)
        home_page.click_and_select_dataview_dropdown("Workflow")
        time.sleep(3)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
