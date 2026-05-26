# test_dropdown_menu.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_dropdown_menu(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()
    time.sleep(5)
    home_page = HomePage(driver)
    home_page.click_and_select_dataview_dropdown("Workflow")
    time.sleep(3)
    print("###########################################################")