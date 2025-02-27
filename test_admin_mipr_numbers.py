# test_admin_mipr_numbers.py
from config import Config
from config import config_browser
from src.pages.login_page import LoginPage
from src.pages.admin_mipr_numbers_page import AdminMiprPage
from locators.locators import *
import time
import pytest

@pytest.mark.selenium
def test_admin_mipr_numbers():
    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        time.sleep(2)
        login_page.login()
        login_page.verify_title()
        driver.get(Config.BASE_URL+AdminMiprNumberLocators.URL)
        admin_mipr_page = AdminMiprPage(driver)
        admin_mipr_page.verify_page_http_200_response(AdminMiprNumberLocators.URL)
        time.sleep(5)
        time.sleep(3)
        admin_mipr_page.click_load_all_miprs()
        time.sleep(20)
        driver.refresh()
        time.sleep(5)
        admin_mipr_page.find_mipr_by_name("DJP TEST")
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        admin_mipr_page.find_mipr_by_user("Pearson")
        time.sleep(5)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()

    time.sleep(3)
    # Close the WebDriver
    driver.quit()
