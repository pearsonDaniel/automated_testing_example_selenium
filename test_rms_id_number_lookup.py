# test_rms_id_number_lookup.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.rms_id_number_lookup_page import RmsIdNumberLookupPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_rms_id_number_lookup():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        time.sleep(2)
        login_page.login()
        login_page.verify_title()
        driver.get(BasePageLocators.BASE_URL+RmsIdNumberLookupLocators.URL)
        rms_id_number_lookup_page = RmsIdNumberLookupPage(driver)
        rms_id_number_lookup_page.verify_page_http_200_response(RmsIdNumberLookupLocators.URL)
        time.sleep(5)
        rms_id_number_lookup_page.verify_dataview_page_title(RmsIdNumberLookupLocators.TITLE, "RMS ID Number Lookup")
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
