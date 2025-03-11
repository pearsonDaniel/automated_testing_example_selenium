# test_all_items_fy.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.all_items_fy_page import AllItemsFYPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_all_items_fy(request):
    browser = request.config.getoption("--browser")
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
    driver.quit()
