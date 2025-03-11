# test_admin_status_update.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_status_update_page import AdminStatusUpdatePage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_status_update():

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
        print("Navigating to: " + str(Config.BASE_URL + AdminStatusUpdateLocators.URL))
        driver.get(Config.BASE_URL+AdminStatusUpdateLocators.URL)
        print("Checking status code of page...")
        admin_status_update_page = AdminStatusUpdatePage(driver)
        admin_status_update_page.verify_page_http_200_response(AdminStatusUpdateLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()

