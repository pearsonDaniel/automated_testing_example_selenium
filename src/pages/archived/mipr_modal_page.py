# mipr_modal_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from locators.locators import *
from src.pages.base_page import BasePage

from datetime import date
from faker import Faker

import time
import random
import os

class MiprModalPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    

    # Create Unique MIPR Title using session user and timestamp
    def enter_mipr_number(self):
        today = date.today()
        formatted_date = today.strftime("%B %d, %Y")
        local_time = time.localtime()
        formatted_time = time.strftime("%H:%M:%S", local_time)
        session_user = os.getlogin()
        print("The current User is: " + str(session_user))
        print("The current time is "+ str(formatted_time))
        mipr_name = "TEST " + str(session_user) + " - " + str(formatted_date) + " - " + str(formatted_time)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.MIPRNUMBERNAME))
        ).send_keys(mipr_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MiprModalLocators.VALIDATEBUTTON))
        ).click()



    # Choose a random amendment between 1 and 15 ***REACT DROPDOWN***
    def enter_amendment(self):
        random_amendment = random.randint(1, 15)
        print("Selecting Amendment: " + str(random_amendment))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MiprModalLocators.AMENDMENTSELECT))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.AMENDMENTSELECT))
        ).send_keys(str(random_amendment))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.AMENDMENTSELECT))
        ).send_keys(Keys.ENTER)
        print("Assigning " + str(random_amendment) + " as react-select-2-option-"+str(random_amendment))
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.AMENDMENTSELECT))
        ).text

    # Choosing RMS ID value ***REACT DROPDOWN***
    def enter_RMS_ID(self):
            rms_ids = ["AT-14-1004", "CB-13-0658", "CT-16-1382", "DS-15-1194", "DT-15-1069", "HT-14-0959",
                        "P1-17-1500", "P1-23-2546","SN-13-0631", "SV-10-0007", "WS-13-0623", "XL-17-12"]
            choice = str(rms_ids[random.randint(0,11)])
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((MiprModalLocators.RMSID))
            ).send_keys(choice)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((MiprModalLocators.RMSID))
            ).send_keys(Keys.ENTER)
            print("RMS ID: " + str(choice))
            return str(choice)
    
    def verify_rms_id(self, rms_id):
        assert WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((MiprModalLocators.RMSID))
            ).text == str(rms_id)

    # # Create random date string and insert into date-picker field
    def email_received_input(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MiprModalLocators.EMAILRECEIVEDDATE))
        ).click()
        month = str(random.randint(1,12))
        day = str(random.randint(1, 25))
        years = [2025, 2026, 2027, 2028, 2029, 2030]
        YEAR = str(years[random.randint(0,5)])
        random_date = month+day+YEAR
        print("Clicking the received date input field...")
        print("Field has been clicked. Attempting to send keys...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.EMAILRECEIVEDDATE))
        ).send_keys(random_date)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.EMAILRECEIVEDDATE))
        ).send_keys(Keys.ENTER)
        self.driver.save_screenshot("test/test_resources/screenshots/email_received_screenshot.png")
        print(str(self.driver.find_element(*MiprModalLocators.EMAILRECEIVEDDATE).get_attribute('value')))
        print("The Date on the form was set to " + str(self.driver.find_element(*MiprModalLocators.EMAILRECEIVEDDATE).get_attribute('value')) + ".")
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.EMAILRECEIVEDDATE))
        ).text


    # # Choose a random primary cor from fixed dropdown list
    def input_primary_cor(self):
        random_primary_cor_index = random.randint(2, 5)
        print(str(random_primary_cor_index))
        dropdown = Select(self.driver.find_element(*MiprModalLocators.PRIMARYCOR))
        dropdown.select_by_index(random_primary_cor_index)
        print("Primary Cor: " + str(dropdown.first_selected_option.text) + " selected.")
        return str(dropdown.first_selected_option.text)

    # # Insert plain text into ACOR Name field
    def input_acor_name(self):
        fake = Faker()
        fake_name = fake.name()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MiprModalLocators.ACORNAME))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.ACORNAME))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.ACORNAME))
        ).send_keys(str(fake_name))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.ACORNAME))
        ).send_keys(Keys.TAB)
        print("ACOR: " + str(fake_name))
        return str(fake_name)

    # Insert random contract amount into the field
    def input_contract_amount(self):
        random_contract_amount = random.randint(0, 10000000)
        print(str(random_contract_amount))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.CONTRACTAMOUNT))
        ).send_keys(str(random_contract_amount))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.CONTRACTAMOUNT))
        ).send_keys(Keys.TAB)
        print("Contract Amount: " + str(random_contract_amount))
        return str(random_contract_amount)
        

    # # Insert random csdc amount into the field
    def input_csdc_amount(self):
        random_csdc_amount = random.randint(0, 1000000)
        print(str(random_csdc_amount))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.CSDCAMOUNT))
        ).send_keys(str(random_csdc_amount))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((MiprModalLocators.CSDCAMOUNT))
        ).send_keys(Keys.TAB)
        print("CDSC Amount: " + str(random_csdc_amount))
        return str(random_csdc_amount)

    # # Choose random service branch by index
    def input_service_branch(self):
        random_service_index = random.randint(1, 6)
        print(str(random_service_index))
        dropdown = Select(self.driver.find_element(*MiprModalLocators.SERVICEBRANCH))
        dropdown.select_by_index(random_service_index)
        print("Service Branch: " + str(dropdown.first_selected_option.text) + " selected.")
        return str(dropdown.first_selected_option.text)
    

    # # Choose determination randomly
    def input_determination(self):
        random_determination_index = random.randint(0, 1)
        print(str(random_determination_index))
        dropdown = Select(self.driver.find_element(*MiprModalLocators.DETERMINATION))
        dropdown.select_by_index(random_determination_index)
        print("Combo MIPR: " + str(dropdown.first_selected_option.text) + " selected.")
        return str(dropdown.first_selected_option.text)
    
    # Clicks Create button to submit the request
    def click_create(self):
        print("Clicking Submit")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MiprModalLocators.CREATEBUTTON))
        ).click()
        time.sleep(1)
        print("Verifying if Create Modal has disappeared...")
        try:
            assert self.driver.find_element(By.XPATH, '//div[@class="modal create-new-mipr"]').is_displayed()
            print("*****FAIL***** THE MODAL FAILED TO CLOSE - MIPR CREATION UNLIKELY")
        except NoSuchElementException:
            print("*****PASS***** THE MODAL IS NO LONGER DISPLAYED - MIPR CREATION PROBABLE")
            pass



