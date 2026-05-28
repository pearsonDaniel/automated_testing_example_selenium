# cart_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.cart_locators import CartLocators
from locators.homepage_locators import HomePageLocators
from locators.checkout_locators import CheckoutLocators
from locators.locators import *
from src.pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def verify_open_cart(self):
        print("Verifying Shopping Cart page is open...")
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CartLocators.CART_TITLE))
        ).text == "Your Cart"
        print("Shopping Cart page verified as open with title: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CartLocators.CART_TITLE))
        ).text))

    def verify_item_in_cart(self, item_name_locator, item_quantity_locator, item_price_locator, expected_name, expected_quantity, expected_price):
        print("Verifying item is in cart with correct name, quantity, and price...")
        actual_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((item_name_locator))
        ).text
        actual_quantity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((item_quantity_locator))
        ).text
        actual_price = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((item_price_locator))
        ).text
        assert actual_name == expected_name, f"Expected item name '{expected_name}', but got '{actual_name}'"
        assert int(actual_quantity) == expected_quantity, f"Expected quantity '{expected_quantity}', but got '{actual_quantity}'"
        assert actual_price == expected_price, f"Expected price '{expected_price}', but got '{actual_price}'"
        print(f"Item verified in cart with name: {actual_name}, quantity: {actual_quantity}, and price: {actual_price}")


    def click_continue_shopping(self):
        print("Clicking 'Continue Shopping' button...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((CartLocators.CONTINUE_SHOPPING_BUTTON))
        ).click()
        print("'Continue Shopping' button clicked...")
        print("Verifying returned to Home Page...")
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HomePageLocators.INVENTORY_TITLE))
        ).text == "Products"
        print("Returned to Home Page verified with title: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((HomePageLocators.INVENTORY_TITLE))
        ).text))

    def click_checkout(self):
        print("Clicking 'Checkout' button...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((CartLocators.CHECKOUT_BUTTON))
        ).click()
        print("'Checkout' button clicked...")
        print("Verifying navigated to Checkout Page...")
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.CHECKOUT_TITLE))
        ).text == "Checkout: Your Information"
        print("Navigated to Checkout Page verified with title: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.CHECKOUT_TITLE))
        ).text))
