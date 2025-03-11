# test_user_workflow.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.user_workflow_page import UserWorkflowPage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_user_workflow():

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
        driver.get(Config.BASE_URL+UserWorkFlowLocators.URL)
        user_workflow_page = UserWorkflowPage(driver)
        user_workflow_page.verify_page_http_200_response(UserWorkFlowLocators.URL)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
