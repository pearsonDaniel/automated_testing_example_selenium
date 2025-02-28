# test_all_items_fy.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.all_items_fy_page import AllItemsFYPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_all_items_fy():

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
        driver.get(Config.BASE_URL+AllItemsFYLocators.URL)
        all_items_fy_page = AllItemsFYPage(driver)
        all_items_fy_page.verify_page_http_200_response(AllItemsFYLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
