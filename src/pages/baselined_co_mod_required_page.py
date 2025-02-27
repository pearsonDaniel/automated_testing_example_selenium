# baselined_co_mod_required_page.py
from src.pages.base_page import BasePage
from locators.locators import *
import time


class BaselinedCOMODRequiredPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    
    def click_columns_toggle(self, modal_title):
        self.driver.find_element(*BaselinedCOMODRequiredLocators.COLUMNS_ICON).click()
        time.sleep(5)
        assert self.driver.find_element(*BaselinedCOMODRequiredLocators.COLUMNS_MODAL_TITLE).text == modal_title
        print("Modal Title Verified - Modal: " + str(self.driver.find_element(*BaselinedCOMODRequiredLocators.COLUMNS_MODAL_TITLE).text))

    def verify_column_options(self):
        columns_list = self.driver.find_element(*BaselinedCOMODRequiredLocators.COLUMNS_LIST)
        print("Scraping webpage for column items...")
        list_items = columns_list.find_elements(By.TAG_NAME, "li")
        print("Adding scraped items to list...")
        item_values = [item.text for item in list_items]
        print("Scraped List: " + str(item_values))
        assert item_values == BaselinedCOMODRequiredLocators.COLUMNS
        print("PASS: Scraped List matches test parameters.")