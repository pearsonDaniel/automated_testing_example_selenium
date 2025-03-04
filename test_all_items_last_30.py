# test_all_items_last_30.py
from config import Config
from config import config_browser
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.all_items_last_30_page import AllItemsLast30Page
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_all_items_last_30():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        time.sleep(3)
        login_page.login()
        time.sleep(3)
        login_page.verify_title()
        home_page = HomePage(driver)
        home_page.click_and_select_dataview_dropdown("All Items - Last 30 Days")
        all_items_last_30_page = AllItemsLast30Page(driver)
        all_items_last_30_page.verify_page_http_200_response(AllItemsLast30Locators.URL)
        time.sleep(2)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
