# base_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import Config
from locators.locators import BasePageLocators
from selenium.webdriver.support.ui import Select


import requests
import time
import datetime

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        print("Verifying  Page Title...")
        assert self.driver.title == BasePageLocators.TITLE
        print("Page Title verified as " + str(self.driver.title))
        print("****************************")

    def verify_text_input(self, input, locator):
        print("Verifying text input value....")
        print("Input: " + str(input))
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator))
        ).text == str(input)
        print("The value is: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator))
        ).text))
    
    def verify_dropdown_input(self, input, locator):
        dropdown = Select(self.driver.find_element(locator))
        print("Verifying text input value....")
        print("Input: " + str(input))
        assert dropdown.first_selected_option.text == str(input) and dropdown.first_selected_option.text != "Select..."
        print("The value is: " + str(dropdown.first_selected_option.text))


    def logout(self):
        print("Attempting to Logout...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((BasePageLocators.ACCOUNT_DROPDOWN))
        ).click()
        print("Dropdown toggled, selecting 'Logout'...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((BasePageLocators.LOGOUT_BUTTON))
        ).click()
        print("Logout button clicked...")
        assert self.driver.current_url == "https://mtt-staging.cldigitalservices.com/"
        print("***PASS: Successfully Logged Out***")



    def verify_page_http_200_response(self, url):
        target_url = str(url)
        if not target_url.startswith(("http://", "https://")):
            target_url = str(Config.BASE_URL) + target_url

        print("Test Verify HTTP Response for: " + target_url)
        try:
            print("Verifying Page HTTP Code...")
            r = requests.head(target_url, allow_redirects=True, timeout=15, verify=False)
            print("Status Code: " + str(r.status_code))
            assert str(r.status_code) == "200" or str(r.status_code).startswith("2")
            print("Connection Successful")
            print("Status Code: " + str(r.status_code))
        except requests.RequestException as err:
            print("Failed to connect.")
            raise AssertionError(f"HTTP check failed for {target_url}: {err}")

        print("****************************")



    def enter_search_term(self, search_term):
        print("Sending keys: " + str(search_term) + " to search box...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((BasePageLocators.SEARCH_BOX))
    ).send_keys(search_term)
        # self.driver.find_element(*BasePageLocators.SEARCH_BOX).send_keys(search_term)
        print("Searching for: " + str(search_term))
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((BasePageLocators.SEARCH_BUTTON))
    ).click()
        # self.driver.find_element(*BasePageLocators.SEARCH_BUTTON).click()

    def verify_search_results(self, search_term):
        print("Verifying Search Results...")
        assert WebDriverWait(self.driver, 10).until(
        EC.text_to_be_present_in_element((BasePageLocators.SEARCH_RESULTS), f"All Items Matching Search '{search_term}'")
    )
        print("Search Results Verified as: " + str(self.driver.find_element(*BasePageLocators.SEARCH_RESULTS).text))



    
