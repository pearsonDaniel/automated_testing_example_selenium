# test_admin_portal.py
from config import Config
from config import config_browser
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.admin_portal_page import AdminPortalPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_admin_portal():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        login_page.verify_title()
        time.sleep(2)
        login_page.login()
        home_page = HomePage(driver)
        home_page.verify_page_http_200_response(HomePageLocators.URL)
        home_page.click_admin_portal()
        admin_portal_page = AdminPortalPage(driver)
        admin_portal_page.verify_page_http_200_response(AdminPortalPageLocators.URL)
        time.sleep(3)
        print("###########################################################")

        # Close the WebDriver
        driver.quit()
