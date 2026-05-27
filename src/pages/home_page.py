# home_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.homepage_locators import HomePageLocators
from locators.locators import *
from src.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    # Function to verify the Home Page Inventory list Title Value
    def verify_inventory_title(self):
        print("Verifying Inventory Title...")
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HomePageLocators.INVENTORY_TITLE))
        ).text == "Products"
        print("Inventory Title verified as: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HomePageLocators.INVENTORY_TITLE))
        ).text))


    # Functions to Add and Remove items from cart, with verification of button text changes to confirm action was successful

    # Accepts two locators as arguments - the first is the locator for the "Add to cart" button, 
    # and the second is the locator for the "Remove" button for the same item. 
    # The function clicks the "Add to cart" button, then waits for the button text to 
    # change to "Remove" to verify that the item was added to the cart successfully.
    def add_item(self, add_item_locator, remove_item_locator):
        print("Attempting to add item to cart...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((add_item_locator))
        ).click()
        WebDriverWait(self.driver, 10).until(
        EC.text_to_be_present_in_element((remove_item_locator), "Remove")
        )
        assert self.driver.find_element(*remove_item_locator).text == "Remove"
        print("***PASS: Item added to cart successfully***")

    # Accepts two locators as arguments - the first is the locator for the "Remove" button, 
    # and the second is the locator for the "Add to cart" button for the same item.
    # The function clicks the "Remove" button, then waits for the button text to 
    # change to "Add to cart" to verify that the item was removed from the cart successfully.
    def remove_item(self, remove_item_locator, add_item_locator):
        print("Attempting to remove item from cart...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((remove_item_locator))
        ).click()
        WebDriverWait(self.driver, 10).until(
        EC.text_to_be_present_in_element((add_item_locator), "Add to cart")
        )
        assert self.driver.find_element(*add_item_locator).text == "Add to cart"
        print("***PASS: Item removed from cart successfully***")

    

