# test_200_all_items_last_30.py
from conftest import Config
from conftest import config_browser
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.all_items_last_30_page import AllItemsLast30Page
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_200_all_items_last_30(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL+AllItemsLast30Locators.URL)
    all_items_last_30_page = AllItemsLast30Page(driver)
    all_items_last_30_page.verify_page_http_200_response(AllItemsLast30Locators.URL)
    time.sleep(2)
    print("###########################################################")
    driver.quit()
