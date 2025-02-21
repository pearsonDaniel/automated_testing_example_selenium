# admin_portal_page.py
from locators.locators import LoginPageLocators
from locators.locators import AdminPortalPageLocators
from src.pages.base_page import BasePage

class AdminPortalPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    
    # def click_mipr_numbers(self):
    #     self.driver.find_element(*AdminPortalPageLocators.MIPR_NUMBERS).click()

