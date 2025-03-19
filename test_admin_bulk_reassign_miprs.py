# test_admin_bulk_reassign_miprs.py
from conftest import Config
from conftest import config_browser
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_numbers_page import AdminMiprPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_bulk_reassign_miprs(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL+AdminMiprNumberLocators.URL)
    admin_mipr_page = AdminMiprPage(driver)
    time.sleep(5)
    admin_mipr_page.find_mipr_by_user("Bragg")
    admin_mipr_page.bulk_reassign_miprs()
    time.sleep(5)
    print("###########################################################")
    driver.quit()


