# base_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import Config
from locators.locators import BasePageLocators
from locators.locators import BaseModalLocators
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
        assert dropdown.first_selected_option.text == str(input) and dropdown.first_selected_option.text is not "Select..."
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
        print("Test Verify HTTP Response for: "+str(Config.BASE_URL)+str(url))
        try:
            print("Verifying Page HTTP Code...")
            r = requests.head(str(Config.BASE_URL)+str(url))
            assert str(r.status_code) == "200"
            print("Connection Successful")
            print("Status Code: " + str(r.status_code))
        except requests.ConnectionError:
            print("Failed to connect.")
            print("Status Code: " + str(r.status_code))

        print("****************************")



    def verify_modal_title(self, modal_title):
        print("Test Verify Modal Title")
        print("-----------------------")
        title = self.driver.find_element(*BaseModalLocators.MODALTITLE).text
        print("Title scraped from webpage: " + str(title))
        print("Title passed in from test: " + modal_title)
        assert str(title) == str(modal_title)
        print("Modal title verified.")
        print("****************************")

    def click_admin_portal(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((BasePageLocators.ADMIN_PORTAL))
    ).click()

    def click_user_guide(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((BasePageLocators.USER_GUIDE))
    ).click()

    def click_patch_notes(self):
        print("Clicking Patch Notes Icon...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((BasePageLocators.PATCH_NOTES))
        ).click()
        print("Verifying Patch Notes Modal...")
        # assert WebDriverWait(self.driver, 10).until(
        # EC.visibility_of_element_located((BasePageLocators.PATCH_NOTES))
        # ).is_displayed() == True
        # assert self.driver.find_element(*BasePageLocators.PATCH_NOTES_BODY).is_displayed() == True
        print("Patch Notes visible on screen.")
        # WebDriverWait(self.driver, 10).until(
        # EC.element_to_be_clickable((BasePageLocators.CLOSE_MODAL_BUTTON))
        # ).click()
        self.driver.find_element(*BasePageLocators.CLOSE_MODAL_BUTTON).click()

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


    def click_and_select_dataview_dropdown(self, dataview_option):
        print("Choosing option: " + str(dataview_option) + " from list...")
        self.driver.find_element(*BasePageLocators.DROPDOWN_MENU).click()
        assert self.driver.find_element(*BasePageLocators.DROPDOWN_LIST).is_displayed() == True
        print("Dropdown items visible - selecting list item...")
        self.driver.find_element(By.LINK_TEXT, dataview_option).click()



    
