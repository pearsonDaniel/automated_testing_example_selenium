# test_search_box.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_search_box(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    login_page.login()
    login_page.verify_title()
    home_page = HomePage(driver)
    home_page.enter_search_term(BasePageLocators.SEARCH_TERM)
    home_page.verify_search_results(BasePageLocators.SEARCH_TERM)
    print("###########################################################")
    driver.quit()
