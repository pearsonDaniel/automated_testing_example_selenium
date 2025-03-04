# base_page.py
from selenium.webdriver.common.by import By
from config import Config
from locators.locators import BasePageLocators
from locators.locators import BaseModalLocators

import requests
import time

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        print("Verifying  Page Title...")
        assert self.driver.title == BasePageLocators.TITLE
        print("Page Title verified as " + str(self.driver.title))
        print("****************************")

    def logout(self):
        print("Attempting to Logout...")
        self.driver.find_element(*BasePageLocators.ACCOUNT_DROPDOWN).click()
        print("Dropdown toggled, selecting 'Logout'...")
        self.driver.find_element(*BasePageLocators.LOGOUT_BUTTON).click()
        print("Logout button clicked...")
        assert self.driver.current_url == "https://mtt-staging.cldigitalservices.com/"
        print("***PASS: Successfully Logged Out***")



    # Latches onto title within an h2
    # def verify_admin_page_title(self, title_locator, admin_title):
    #     print("Test Verify Admin Page Title")
    #     title = self.driver.find_element(By.XPATH, title_locator).text
    #     print("Title scraped from page: " + title)
    #     print("Title passed in from test: " + admin_title)
    #     print("Verifying...")
    #     assert str(admin_title) == str(title)
    #     print("Admin Page Title verified as: " + str(title))
    #     print("****************************")


    # Latches onto title within an h3
    # def verify_dataview_page_title(self, title_locator, title_value):
    #     print("Test Verify DataView Page Title")
    #     title = self.driver.find_element(By.XPATH, title_locator).text
    #     print("Title scraped from page: " + title)
    #     print("Title passed in from test: " + title_value)
    #     print("Verifying...")
    #     assert str(title) == str(title_value)
    #     print("DataView Title verified as: " + str(title))
    #     print("****************************")



    def verify_page_http_200_response(self, url):
        print("Test Verify HTTP Response for: "+str(Config.BASE_URL)+str(url))
        try:
            print("Verifying Page HTTP Code...")
            r = requests.head(str(Config.BASE_URL)+str(url))
            assert str(r.status_code) == "200" or "307"
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
         self.driver.find_element(*BasePageLocators.ADMIN_PORTAL).click()

    def click_user_guide(self):
         self.driver.find_element(*BasePageLocators.USER_GUIDE).click()

    def click_patch_notes(self):
        print("Clicking Patch Notes Icon...")
        icons = self.driver.find_elements(*BasePageLocators.PATCH_NOTES)
        patch_notes = icons[1]
        patch_notes.click()
        print("Verifying Patch Notes Modal...")
        time.sleep(3)
        assert self.driver.find_element(*BasePageLocators.PATCH_NOTES_BODY).is_displayed() == True
        print("Patch Notes visible on screen.")
        self.driver.find_element(*BasePageLocators.CLOSE_MODAL_BUTTON).click()

    def enter_search_term(self, search_term):
        print("Sending keys: " + str(search_term) + " to search box...")
        self.driver.find_element(*BasePageLocators.SEARCH_BOX).send_keys(search_term)
        print("Searching for: " + str(search_term))
        self.driver.find_element(*BasePageLocators.SEARCH_BUTTON).click()

    def verify_search_results(self, search_term):
        print("Verifying Search Results...")
        assert self.driver.find_element(*BasePageLocators.SEARCH_RESULTS).text == f"All Items Matching Search '{search_term}'"
        print("Search Results Verified as: " + str(self.driver.find_element(*BasePageLocators.SEARCH_RESULTS).text))


    def click_and_select_dataview_dropdown(self, dataview_option):
        print("Choosing option: " + str(dataview_option) + " from list...")
        self.driver.find_element(*BasePageLocators.DROPDOWN_MENU).click()
        assert self.driver.find_element(*BasePageLocators.DROPDOWN_LIST).is_displayed() == True
        print("Dropdown items visible - selecting list item...")
        self.driver.find_element(By.LINK_TEXT, dataview_option).click()



    
