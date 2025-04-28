# test_200_admin_excel_import.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.admin_excel_import_page import AdminExcelImportPage
from locators.locators import *
import pytest


@pytest.mark.selenium
def test_200_admin_excel_import(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    driver.get(Config.BASE_URL + AdminExcelImportLocators.URL)
    admin_excel_import_page = AdminExcelImportPage(driver)
    admin_excel_import_page.verify_page_http_200_response(AdminStatusUpdateLocators.URL)
    print("###########################################################")