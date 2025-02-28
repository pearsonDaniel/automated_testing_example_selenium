# test_admin_users.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.admin_users_page import AdminUsersPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_users():
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
        driver.get(Config.BASE_URL+AdminUsersLocators.URL)
        time.sleep(3)
        admin_users_page = AdminUsersPage(driver)
        admin_users_page.verify_page_http_200_response(AdminUsersLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
    
    