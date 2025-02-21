# test_admin_mipr_lifecycle.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_lifecycle_page import AdminMiprLifeCyclePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_admin_mipr_lifecycle():

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
        driver.get(BasePageLocators.BASE_URL + AdminMiprLifeCycleLocators.URL)
        admin_mipr_lifecycle_page = AdminMiprLifeCyclePage(driver)
        admin_mipr_lifecycle_page.verify_page_http_200_response(AdminMiprLifeCycleLocators.URL)
        admin_mipr_lifecycle_page.verify_title()
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
