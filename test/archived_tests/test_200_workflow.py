# test_200_workflow.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.user_workflow_page import UserWorkflowPage
from locators.locators import *
import pytest
import time

@pytest.mark.selenium
def test_200_workflow(config_browser):
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    driver.get(Config.BASE_URL+UserWorkFlowLocators.URL)
    user_workflow_page = UserWorkflowPage(driver)
    user_workflow_page.verify_page_http_200_response(UserWorkFlowLocators.URL)
    print("###########################################################")