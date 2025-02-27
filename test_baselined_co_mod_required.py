# test_baselined_co_mod_required.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.baselined_co_mod_required_page import BaselinedCOMODRequiredPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_baselined_co_mod_required():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        time.sleep(2)
        login_page.login()
        time.sleep(2)
        login_page.verify_title()
        time.sleep(5)
        baselined_co_mod_required_page = BaselinedCOMODRequiredPage(driver)
        baselined_co_mod_required_page.click_and_select_dataview_dropdown(BaselinedCOMODRequiredLocators.DROPDOWN_LINKTEXT)
        baselined_co_mod_required_page.verify_page_http_200_response(BaselinedCOMODRequiredLocators.URL)
        time.sleep(10)
        # baselined_co_mod_required_page.click_columns_toggle("Manage Columns")
        # time.sleep(2)
        # baselined_co_mod_required_page.verify_column_options()
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
