# test_admin_status_update.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.admin_status_update_page import AdminStatusUpdatePage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_status_update():

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
        print("Navigating to: " + str(BasePageLocators.BASE_URL + AdminStatusUpdateLocators.URL))
        driver.get(BasePageLocators.BASE_URL+AdminStatusUpdateLocators.URL)
        print("Checking status code of page...")
        admin_status_update_page = AdminStatusUpdatePage(driver)
        admin_status_update_page.verify_title()
        admin_status_update_page.verify_page_http_200_response(AdminStatusUpdateLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()

