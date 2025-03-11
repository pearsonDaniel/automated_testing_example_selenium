# test_patch_notes.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_patch_notes(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()
    time.sleep(5)
    home_page = HomePage(driver)
    home_page.click_patch_notes()
    time.sleep(3)
    print("###########################################################")
    driver.quit()
