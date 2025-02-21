# test_verify_columns.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_verify_columns():

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
        time.sleep(3)
        home_page = HomePage(driver)
        home_page.click_columns_toggle("Manage Columns")
        time.sleep(2)
        home_page.verify_column_options()
        time.sleep(3)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
