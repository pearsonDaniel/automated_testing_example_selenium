# test_admin_tabs.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.admin_portal_page import AdminPortalPage
from src.pages.admin_tabs_page import AdminTabsPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_tabs():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Edge":
            driver = webdriver.Edge()
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        print("Running Test in: " + browser)
        driver.get(BasePageLocators.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        time.sleep(2)
        login_page.login()
        login_page.verify_title()
        driver.get(BasePageLocators.BASE_URL+AdminTabsLocators.URL)
        admin_tabs_page = AdminTabsPage(driver)
        admin_tabs_page.verify_title()
        admin_tabs_page.verify_page_http_200_response(AdminTabsLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
   