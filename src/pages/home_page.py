# home_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import *
from src.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

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

    

