# test_200_admin_data_report.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.admin_mipr_data_report_page import AdminMiprDataReportPage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_admin_data_report(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    home_page = HomePage(driver)
    driver.get(Config.BASE_URL + AdminMiprDataReportLocators.URL)
    admin_mipr_data_report_page = AdminMiprDataReportPage(driver)
    admin_mipr_data_report_page.verify_page_http_200_response(AdminMiprDataReportLocators.URL)
    print("###########################################################")