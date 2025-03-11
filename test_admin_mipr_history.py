# test_admin_mipr_history.py
from conftest import Config
from conftest import config_browser
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_history_page import AdminMiprHistoryPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_mipr_history(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    time.sleep(2)
    login_page.login()
    login_page.verify_title()
    driver.get(Config.BASE_URL+AdminMiprHistoryLocators.URL)
    admin_mipr_history_page = AdminMiprHistoryPage(driver)
    admin_mipr_history_page.verify_page_http_200_response(AdminMiprHistoryLocators.URL)
    print("###########################################################")
    driver.quit()

