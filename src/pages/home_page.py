# home_page.py
from locators.locators import *
from src.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_create_mipr(self):
        self.driver.find_element(*HomePageLocators.CREATEMIPRBUTTON).click()

    
    def click_export_report(self):
        self.driver.find_element(*HomePageLocators.EXPORTREPORT).click()


    def click_columns_toggle(self, modal_title):
        self.driver.find_element(*HomePageLocators.COLUMNSICON).click()
        assert self.driver.find_element(*BaseModalLocators.MODALTITLE).text == modal_title
        print("Modal Title Verified - Modal: " + str(self.driver.find_element(*BaseModalLocators.MODALTITLE).text))

    def verify_column_options(self):
        columns_list = self.driver.find_element(*HomePageLocators.COLUMNSLIST)
        print("Scraping webpage for column items...")
        list_items = columns_list.find_elements(By.TAG_NAME, "li")
        print("Adding scraped items to list...")
        item_values = [item.text for item in list_items]
        print("Scraped List: " + str(item_values))
        assert item_values == HomePageLocators.COLUMNS
        print("PASS: Scraped List matches test parameters.")



    def check_phase_checkbox(self, phase_locator, phase_string, phase_total, checked_status1, checked_status2):
        # This is the text from the "Records Found at the bottom of the page"
        record_string = str(self.driver.find_element(By.CSS_SELECTOR, HomePageLocators.FOUNDRECORDSTOTAL).text)
        # We parse through the text to extract the number as an integer and insert it into a list
        total_records_found = [int(s) for s in record_string.split() if s.isdigit()]

        # Here we take the passed in argument of phase and get the text value of the phase
        phase = str(self.driver.find_element(By.XPATH, phase_locator).get_attribute('value'))
        # This is the number field associated with the current phase
        current_phase_total = int(self.driver.find_element(By.CSS_SELECTOR, phase_total).text)
        print("Phase: " + phase + " - " + "Total: " + str(current_phase_total))
        # If we need to refer to the total records found, we can by pointing to the 1st element in the list
        print("Total Records Found: " + str(int(total_records_found[0])))

        # Calculating the predictive phase total before checking or unchecking the 
        # checkbox of the phase and will be compared against later
        if checked_status1 == HomePageLocators.CHECKEDSTATUS:
            predictive_record_total = int(total_records_found[0]) - current_phase_total
            print("After unchecking the checkbox, the total records found should be: " + str(predictive_record_total))
        else:
            predictive_record_total = int(total_records_found[0]) + current_phase_total
            print("After checking the checkbox, the total records found should be: " + str(predictive_record_total))
            
        # Determing the status of the Checkbox by checking the class of the parent li element
        print("The status of the checkbox is: " + str(checked_status1))
        assert str(self.driver.find_element(By.XPATH, phase_locator).find_element(By.XPATH, '..').get_attribute('class')) == str(checked_status1)
       
        # Verifying the correct checkbox is being selected before clicking the checkbox
        print(str("Value within checkbox: " + self.driver.find_element(By.XPATH, phase_locator).get_attribute('value')))
        assert self.driver.find_element(By.XPATH, phase_locator).get_attribute('value') == str(phase_string)
        # Click checkbox
        print("Clicking checkbox...")
        self.driver.find_element(By.XPATH, phase_locator).click()

        # Determining the updated status of the Checkbox
        print("The status of the checkbox is: " + str(checked_status2))
        assert str(self.driver.find_element(By.XPATH, phase_locator).find_element(By.XPATH, '..').get_attribute('class')) == str(checked_status2)
       
        # If the checkbox was successfully checked or unchecked, we now verify the number of records found
        new_record_string = str(self.driver.find_element(By.CSS_SELECTOR, HomePageLocators.FOUNDRECORDSTOTAL).text)
        updated_total_records_found = [int(s) for s in new_record_string.split() if s.isdigit()]
        print("Updated total records found: " + str(updated_total_records_found[0]))
        print("Verifying...")
        assert predictive_record_total == updated_total_records_found[0]
        print("Verification Complete")
        print("*********************************************************")
    
    
    # def uncheck_phase_checkbox(self, phase_locator, phase_string):
    #     print("Asserting that the checkbox has been unchecked")
    #     assert str(self.driver.find_element(By.XPATH, phase_locator).find_element(By.XPATH, '..').get_attribute('class')) == 'horizontal-phase-menu-list-item '
    #     print("Asserting checkbox is the correct Phase.")
    #     print(str("Value within checkbox: " + self.driver.find_element(By.XPATH, phase_locator).get_attribute('value')))
    #     assert self.driver.find_element(By.XPATH, phase_locator).get_attribute('value') == str(phase_string)
    #     self.driver.find_element(By.XPATH, phase_locator).click()
    #     print("Asserting the checkbox is active")
    #     assert str(self.driver.find_element(By.XPATH, phase_locator).find_element(By.XPATH, '..').get_attribute('class')) == 'horizontal-phase-menu-list-item active'
       

    # def click_logging_phase_checkbox(self):
    #     print("Asserting the checkbox is active")
    #     assert str(self.driver.find_element(*HomePageLocators.LOGGING).find_element(By.XPATH, '..').get_attribute('class')) == 'horizontal-phase-menu-list-item active'
    #     print("Asserting checkbox is Logging Phase.")
    #     print(str("Value within checkbox: " + self.driver.find_element(*HomePageLocators.LOGGING).get_attribute('value')))
    #     assert self.driver.find_element(*HomePageLocators.LOGGING).get_attribute('value') == "Logging"
    #     self.driver.find_element(*HomePageLocators.LOGGING).click()
    #     print("Asserting that the checkbox has been unchecked")
    #     assert str(self.driver.find_element(*HomePageLocators.LOGGING).find_element(By.XPATH, '..').get_attribute('class')) == 'horizontal-phase-menu-list-item '



    # def click_evaluating_phase_checkbox(self):
    #     print("Asserting the checkbox is active")
    #     assert str(self.driver.find_element(*HomePageLocators.EVALUATING).find_element(By.XPATH, '..').get_attribute('class')) == 'horizontal-phase-menu-list-item active'
    #     print("Asserting checkbox is Evaluating Phase.")
    #     print(str("Value within checkbox: " + self.driver.find_element(*HomePageLocators.EVALUATING).get_attribute('value')))
    #     assert self.driver.find_element(*HomePageLocators.EVALUATING).get_attribute('value') == "Evaluating"
    #     self.driver.find_element(*HomePageLocators.EVALUATING).click()
    #     print("Asserting that the checkbox has been unchecked")
    #     assert str(self.driver.find_element(*HomePageLocators.EVALUATING).find_element(By.XPATH, '..').get_attribute('class')) == 'horizontal-phase-menu-list-item '


