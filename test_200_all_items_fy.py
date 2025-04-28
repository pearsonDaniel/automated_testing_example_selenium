# test_200_all_items_fy.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.all_items_fy_page import AllItemsFYPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_200_all_items_fy(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL+AllItemsFYLocators.URL)
    all_items_fy_page = AllItemsFYPage(driver)
    all_items_fy_page.verify_page_http_200_response(AllItemsFYLocators.URL)
    print("###########################################################")