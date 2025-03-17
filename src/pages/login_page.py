# login_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import LoginPageLocators
from src.pages.base_page import BasePage
import openpyxl

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
        # Maximize the window
        self.driver.maximize_window()

        # Wait for fields to load before interacting with them
        username_field = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((LoginPageLocators.USERNAME_FIELD))
    )
        password_field = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((LoginPageLocators.PASSWORD_FIELD))
    )
        login_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((LoginPageLocators.LOGIN_BUTTON))
    )

        # Interacting with the login fields after loading
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
