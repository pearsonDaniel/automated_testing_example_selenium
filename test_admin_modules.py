# test_admin_modules.py
from config import Config
from config import config_browser
from src.pages.login_page import LoginPage
from src.pages.admin_modules_page import AdminModulesPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_modules():

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
        driver.get(BasePageLocators.BASE_URL+AdminModulesLocators.URL)
        admin_modules_page = AdminModulesPage(driver)
        admin_modules_page.verify_page_http_200_response(AdminModulesLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()