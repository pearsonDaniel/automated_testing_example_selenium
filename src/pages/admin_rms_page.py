# admin_rms_page.py
from locators.locators import *
from src.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class AdminRMSPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_add_rms_id_number(self):
        self.driver.find_element(*AdminRMSLocators.ADDRMSBUTTON).click()
    
    

    def input_rms_id_number(self, browser):
        print("Adding the RMS ID in " + browser)
        self.driver.find_element(*AdminRMSLocators.MODALRMSIDNUMBER).send_keys("Test RMS Number " + browser)

    def select_cor(self):
        print("Selecting COR...")
        index = random.randint(1,9)
        select = Select(self.driver.find_element(*AdminRMSLocators.MODALRMSCORSELECT))
        select.select_by_index(index)
        print(str(select.first_selected_option.text) + " set as COR.")
        assert select.first_selected_option.text != "Select COR"
        assert select.first_selected_option.text != None
    
    def select_priority(self):
        print("Setting priority....")
        index = random.randint(0,3)
        select = Select(self.driver.find_element(*AdminRMSLocators.MODALRMSPRIORITYSELECT))
        select.select_by_index(index)
        print("Priority set to: " + str(select.first_selected_option.text))
    
    def select_active(self):
        print("Setting Active status...")
        index = random.randint(0,1)
        select = Select(self.driver.find_element(*AdminRMSLocators.MODALRMSACTIVESELECT))
        select.select_by_index(index)
        print("Active status set to: " + str(select.first_selected_option.text))

    def click_create_button(self):
        print("Creating RMS ID Number....")
        self.driver.find_element(*AdminRMSLocators.MODALRMSCREATEBUTTON).click()


    # Methods for searching and deleting an RMS ID Number

    def search_rms_id(self):
        self.driver.find_element(*AdminRMSLocators.RMSSEARCH).send_keys("Test RMS Number Firefox")
        time.sleep(15)
        # first_result = self.driver.find_element(By.XPATH, '//div[@col-id="Ord_Name"]')
        first_result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Test RMS Number Firefox')]")))
        print(str(first_result.text))
        assert first_result.text == "Test RMS Number Firefox"

    # def delete_rms_id(self):
    #     # time.sleep(5)
    #     # self.driver.find_element(*AdminRMSLocators.RMSSEARCH).send_keys("Test RMS Number Firefox")
    #     # time.sleep(10)
    #     first_result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Test RMS Number Firefox')]")))

    #     if first_result:
    #         delete_button = self.driver.find_element(By.XPATH, '')
    #         self.driver.execute_script('arguments[0].scrollIntoView(true)', delete_button);            time.sleep(5)
    #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(delete_button)).click()
    #         confirm_delete = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div/div[3]/div/div/div[4]/div/div/button[1]')))
    #         confirm_delete.click()
    #     else:
    #         print("Could not find TEST RMS ID Firefox record in DataView....")



    
    
