# test_200_admin_mipr_lifecycle.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_lifecycle_page import AdminMiprLifeCyclePage
from locators.locators import *
import pytest


@pytest.mark.selenium
def test_200_admin_mipr_lifecycle(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL + AdminMiprLifeCycleLocators.URL)
    admin_mipr_lifecycle_page = AdminMiprLifeCyclePage(driver)
    admin_mipr_lifecycle_page.verify_page_http_200_response(AdminMiprLifeCycleLocators.URL)
    print("###########################################################")
    driver.quit()
