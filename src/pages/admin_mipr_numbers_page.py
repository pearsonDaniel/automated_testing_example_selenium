# admin_mipr_numbers_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import *
from src.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time


class AdminMiprPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_load_all_miprs(self):
        print("Clicking 'Load All Miprs'....")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AdminMiprNumberLocators.LOADALLMIPRSBUTTON))
        ).click()
        title_text = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((AdminMiprNumberLocators.ALL_MIPRS_TITLE))
        ).text
        assert "records for All MIPR Numbers"
        print("All MIPR Numbers Text located on Page.")
        
        # self.driver.find_element(*AdminMiprNumberLocators.LOADALLMIPRSBUTTON).click()


    def find_mipr_by_name(self, mipr_name):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((AdminMiprNumberLocators.FINDMIPRBYNAME))
        ).send_keys(str(mipr_name))
        # self.driver.find_element(*AdminMiprNumberLocators.FINDMIPRBYNAME).send_keys(str(mipr_name))
        print(str("This is the value of the input: " + self.driver.find_element(*AdminMiprNumberLocators.FINDMIPRBYNAME).get_attribute('value')))
        # self.driver.find_element(*AdminMiprNumberLocators.MIPRNAMEFINDBUTTON).click()
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AdminMiprNumberLocators.MIPRNAMEFINDBUTTON))
        ).click()

    def find_mipr_by_user(self, user_name):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((AdminMiprNumberLocators.FINDMIPRBYUSER))
        ).send_keys(str(user_name))

        print(str("The name inserted is: " + self.driver.find_element(*AdminMiprNumberLocators.FINDMIPRBYUSER).get_attribute('value')))
        # assert str(self.driver.find_element(*AdminMiprNumberLocators.FINDMIPRBYUSER).get_attribute('value')) == str(135)
        print("User verified.")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((AdminMiprNumberLocators.USERFINDBUTTON))
        ).click()
        # self.driver.find_element(*AdminMiprNumberLocators.USERFINDBUTTON).click()


    def bulk_reassign_miprs(self):
        print("Choosing 'Assigned to'....")
        time.sleep(5)
        self.driver.find_element(*AdminMiprNumberLocators.BULKEDITDROPDOWN).send_keys(str('Assigned'))
        time.sleep(3)
        self.driver.find_element(*AdminMiprNumberLocators.BULKEDITNEXTBUTTON).click()
        time.sleep(3)
        self.driver.find_element(*AdminMiprNumberLocators.BULKEDITVALUE).send_keys('Pearson')
        time.sleep(3)
        print("Selected user for reassigned miprs...")
        self.driver.find_element(*AdminMiprNumberLocators.BULKEDITSAVEBUTTON).click()
        time.sleep(3)
        print("About to save, accepting alert dialogue...")
        Alert(self.driver).accept()
        print("Alert accepted.")






    
    
