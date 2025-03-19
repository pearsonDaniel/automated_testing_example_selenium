# test_create_mipr.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.mipr_modal_page import MiprModalPage
import time
import pytest

@pytest.mark.selenium
def test_create_mipr(request):
    # Instantiate Driver instance
    browser = request.config.getoption("--browser")
    driver = config_browser(browser)
    driver.get(Config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    # Instantiate HomePage instance and click Create MIPR
    home_page = HomePage(driver)
    time.sleep(5)
    home_page.click_create_mipr()
    # Perform actions to create MIPR
    mipr_modal = MiprModalPage(driver)
    mipr_modal.enter_mipr_number(browser)
    mipr_modal.enter_amendment()
    mipr_modal.enter_RMS_ID()
    mipr_modal.email_received_input(browser)
    mipr_modal.input_primary_cor()
    mipr_modal.input_acor_name()
    mipr_modal.input_contract_amount()
    mipr_modal.input_csdc_amount()
    mipr_modal.input_service_branch()
    mipr_modal.input_determination()
    mipr_modal.click_create()
    print("####################################################")
    driver.quit()