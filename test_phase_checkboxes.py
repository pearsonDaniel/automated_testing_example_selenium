# test_phase_checkboxes.py
from config import config_browser
from config import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_phase_checkboxes():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        driver = config_browser(browser)
        driver.get(Config.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        login_page.login()
        time.sleep(2)
        home_page = HomePage(driver)
        home_page.verify_page_http_200_response(HomePageLocators.URL)
        time.sleep(5)

        # Checking and unchecking the checkboxes
        home_page.check_phase_checkbox(HomePageLocators.LOGGING, "Logging", HomePageLocators.LOGGINGTOTAL, HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.LOGGING, "Logging", HomePageLocators.LOGGINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.EVALUATING, "Evaluating", HomePageLocators.EVALUATINGTOTAL , HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.EVALUATING, "Evaluating", HomePageLocators.EVALUATINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.PROCESSING, "Processing", HomePageLocators.PROCESSINGTOTAL, HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.PROCESSING, "Processing", HomePageLocators.PROCESSINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.OBLIGATING, "Obligating", HomePageLocators.OBLIGATINGTOTAL,  HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.OBLIGATING, "Obligating", HomePageLocators.OBLIGATINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.COMPLETED, "Completed", HomePageLocators.COMPLETEDTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        
        home_page.check_phase_checkbox(HomePageLocators.COMPLETED, "Completed", HomePageLocators.COMPLETEDTOTAL, HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        time.sleep(2)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
