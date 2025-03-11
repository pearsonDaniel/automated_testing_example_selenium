# test_export_report.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest
import os



@pytest.mark.selenium
def test_export_report(request):
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    time.sleep(3)
    login_page = LoginPage(driver)
    login_page.verify_page_http_200_response(LoginPageLocators.URL)
    time.sleep(2)
    login_page.login()
    time.sleep(3)
    home_page = HomePage(driver)
    time.sleep(2)
    home_page.click_export_report()
    time.sleep(5)
    file_path = r"C:\Users\daniel.pearson\Downloads\export (30)" # Raw string to handle backslashes in Windows paths

    if os.path.exists(file_path):
        print(f"File exists at: {file_path}")
        if os.path.isfile(file_path):
            print("This is a file")
        else:
            print("This is not a file.")
    else:
        print(f"File does not exist at: {file_path}")
    print("###########################################################")
    
    driver.quit()
