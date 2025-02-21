# login_page.py
from locators.locators import LoginPageLocators
from src.pages.base_page import BasePage
import openpyxl
import time

# Getting the spreadsheet
spreadsheet = openpyxl.load_workbook(r"test\test_resources\user_credentials.xlsx")
# Getting the active sheet
credentials = spreadsheet.active
# Get login credentials from two cells and store them into variables to be used
username = credentials.cell(row=2, column=1).value
password = credentials.cell(row=2, column=2).value

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    
    def login(self):
        self.driver.maximize_window()
        time.sleep(3)
        try:
            self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)
        except Exception:
            print("Could not find username field.")
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
