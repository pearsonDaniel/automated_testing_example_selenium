# test_admin_mipr_numbers.py
from conftest import Config
from conftest import config_browser
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_numbers_page import AdminMiprPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_mipr_numbers(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL+AdminMiprNumberLocators.URL)
    # time.sleep(3)
    admin_mipr_page = AdminMiprPage(driver)
    admin_mipr_page.click_load_all_miprs()
    # admin_mipr_page.find_mipr_by_name("DJP TEST")
    # admin_mipr_page.find_mipr_by_user("Pearson")
    print("###########################################################")