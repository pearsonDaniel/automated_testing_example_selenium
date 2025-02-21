# test_create_mipr.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.mipr_modal_page import MiprModalPage
import time
import pytest

@pytest.mark.selenium
def test_create_mipr():
    # Instantiate Driver instance
    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Edge":
            driver = webdriver.Edge()
        elif browser == "Firefox":
            driver = webdriver.Firefox()
    #Navigate to Login Page and login
        print("Running Test in: " + str(browser))
        driver.get("https://mtt-staging.cldigitalservices.com/")
        login_page = LoginPage(driver)
        login_page.login()
        # Instantiate HomePage instance and click Create MIPR
        home_page = HomePage(driver)
        time.sleep(5)
        home_page.click_create_mipr()
        # Perform actions to create MIPR
        mipr_modal = MiprModalPage(driver)
        mipr_modal.enter_mipr_number(browser)
        time.sleep(5)
        mipr_modal.enter_amendment()
        time.sleep(3)
        mipr_modal.enter_RMS_ID()
        time.sleep(3)
        mipr_modal.email_received_input(browser)
        mipr_modal.input_primary_cor()
        mipr_modal.input_acor_name()
        mipr_modal.input_contract_amount()
        mipr_modal.input_csdc_amount()
        mipr_modal.input_service_branch()
        mipr_modal.input_determination()
        time.sleep(5)
        mipr_modal.click_create()
        print("####################################################")
        driver.quit()