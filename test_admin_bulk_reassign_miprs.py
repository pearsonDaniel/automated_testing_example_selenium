# test_admin_bulk_reassign_miprs.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_numbers_page import AdminMiprPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_bulk_reassign_miprs():
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
        time.sleep(2)
        login_page.login()
        driver.get(BasePageLocators.BASE_URL+AdminMiprNumberLocators.URL)
        admin_mipr_page = AdminMiprPage(driver)
        admin_mipr_page.verify_title()
        admin_mipr_page.verify_page_http_200_response(AdminMiprNumberLocators.URL)
        time.sleep(5)
        admin_mipr_page.find_mipr_by_user("Bragg")
        admin_mipr_page.bulk_reassign_miprs()
        time.sleep(5)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()


