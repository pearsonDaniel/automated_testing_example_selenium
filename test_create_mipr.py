# test_create_mipr.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.mipr_modal_page import MiprModalPage
from locators.locators import MiprModalLocators
import time
import pytest

@pytest.mark.selenium
def test_create_mipr(config_browser):
    # Instantiate Driver instance
    driver = config_browser
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    # Instantiate HomePage instance and click Create MIPR
    home_page = HomePage(driver)
    home_page.click_create_mipr()
    # Perform actions to create MIPR
    mipr_modal = MiprModalPage(driver)
    mipr_modal.enter_mipr_number()
    amendment = mipr_modal.enter_amendment()
    mipr_modal.verify_text_input(amendment, MiprModalLocators.AMENDMENTSELECT)
    rms_id = mipr_modal.enter_RMS_ID()
    mipr_modal.verify_text_input(rms_id, MiprModalLocators.RMSID)
    email_received = mipr_modal.email_received_input()
    mipr_modal.verify_text_input(email_received, MiprModalLocators.EMAILRECEIVEDDATE)
    primary_cor = mipr_modal.input_primary_cor()
    mipr_modal.verify_text_input(primary_cor, MiprModalLocators.PRIMARYCOR)
    acor = mipr_modal.input_acor_name()
    mipr_modal.verify_text_input(acor, MiprModalLocators.ACORNAME)
    contract_amount = mipr_modal.input_contract_amount()
    mipr_modal.verify_text_input(contract_amount, MiprModalLocators.CONTRACTAMOUNT)
    csdc_amount = mipr_modal.input_csdc_amount()
    mipr_modal.verify_text_input(csdc_amount, MiprModalLocators.CSDCAMOUNT)
    service_branch = mipr_modal.input_service_branch()
    mipr_modal.verify_text_input(service_branch, MiprModalLocators.SERVICEBRANCH)
    determination = mipr_modal.input_determination()
    mipr_modal.verify_text_input(determination, MiprModalLocators.DETERMINATION)
    mipr_modal.click_create()
    print("####################################################")