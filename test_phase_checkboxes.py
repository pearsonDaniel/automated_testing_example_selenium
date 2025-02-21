# test_phase_checkboxes.py
from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.locators import *
import time
import pytest


@pytest.mark.selenium
def test_phase_checkboxes():

    browsers = ["Chrome", "Edge", "Firefox"]
    for browser in browsers:
        if browser == "Chrome":
            driver = webdriver.Chrome()
        elif browser == "Edge":
            driver = webdriver.Edge()
        elif browser == "Firefox":
            driver = webdriver.Firefox()
        print("Running Test in: " + browser)
        driver.get(BasePageLocators.BASE_URL)
        time.sleep(3)
        login_page = LoginPage(driver)
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        time.sleep(2)
        login_page.login()
        home_page = HomePage(driver)
        home_page.verify_page_http_200_response(HomePageLocators.URL)
        time.sleep(5)
        home_page.check_phase_checkbox(HomePageLocators.LOGGING, "Logging", HomePageLocators.LOGGINGTOTAL, HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.LOGGING, "Logging", HomePageLocators.LOGGINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.EVALUATING, "Evaluating", HomePageLocators.EVALUATINGTOTAL , HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.EVALUATING, "Evaluating", HomePageLocators.EVALUATINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.PROCESSING, "Processing", HomePageLocators.PROCESSINGTOTAL, HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.PROCESSING, "Processing", HomePageLocators.PROCESSINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.OBLIGATING, "Obligating", HomePageLocators.OBLIGATINGTOTAL,  HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.OBLIGATING, "Obligating", HomePageLocators.OBLIGATINGTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.COMPLETED, "Completed", HomePageLocators.COMPLETEDTOTAL, HomePageLocators.UNCHECKEDSTATUS, HomePageLocators.CHECKEDSTATUS)
        # time.sleep(2)
        home_page.check_phase_checkbox(HomePageLocators.COMPLETED, "Completed", HomePageLocators.COMPLETEDTOTAL, HomePageLocators.CHECKEDSTATUS, HomePageLocators.UNCHECKEDSTATUS)
        time.sleep(2)
        # home_page.uncheck_phase_checkbox(HomePageLocators.LOGGING, "Logging")
        # time.sleep(5)
        # home_page.click_logging_phase_checkbox()
        # time.sleep(5)
        # home_page.click_evaluating_phase_checkbox()
        # time.sleep(5)
        # home_page.click_processing_phase_checkbox()
        # time.sleep(5)
        # home_page.click_obligating_phase_checkbox()
        # time.sleep(5)
        # home_page.click_completed_phase_checkbox()
        # time.sleep(5)
        print("###########################################################")
        # Close the WebDriver
        driver.quit()
