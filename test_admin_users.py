# test_admin_users.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.admin_portal_page import AdminPortalPage
from src.pages.admin_mipr_numbers_page import AdminMiprPage
from src.pages.admin_users_page import AdminUsersPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_users():
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
        driver.get(BasePageLocators.BASE_URL+AdminUsersLocators.URL)
        admin_users_page = AdminUsersPage(driver)
        admin_users_page.verify_title()
        admin_users_page.verify_page_http_200_response(AdminUsersLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
    
    