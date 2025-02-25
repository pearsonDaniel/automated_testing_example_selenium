# test_admin_status.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.admin_status_page import AdminStatusPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_status():

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
        driver.get(BasePageLocators.BASE_URL+AdminStatusLocators.URL)
        admin_status_page = AdminStatusPage(driver)
        admin_status_page.verify_title()
        admin_status_page.verify_page_http_200_response(AdminStatusLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()

