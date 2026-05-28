# checkout_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.cart_locators import CartLocators
from locators.homepage_locators import HomePageLocators
from locators.checkout_locators import CheckoutLocators
from locators.locators import *
from src.pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def add_checkout_info(self, first_name, last_name, postal_code):
        print("Adding checkout information...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.CHECKOUT_TITLE))
        ).text == "Checkout: Your Information"
        print("Checkout Page verified with title: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.CHECKOUT_TITLE))
        ).text))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.FIRST_NAME_FIELD))
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.LAST_NAME_FIELD))
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.POSTAL_CODE_FIELD))
        ).send_keys(postal_code)

    def click_continue(self):
        print("Clicking 'Continue' button...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((CheckoutLocators.CONTINUE_BUTTON))
        ).click()
        print("'Continue' button clicked...")
        print("Verifying navigated to Checkout Overview Page...")
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.CHECKOUT_TITLE))
        ).text == "Checkout: Overview"
        print("Navigated to Checkout Overview Page verified with title: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.CHECKOUT_TITLE))
        ).text))

    def verify_payment_info(self, expected_payment_info):
        print("Verifying payment information...")
        actual_payment_info = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.PAYMENT_INFORMATION_VALUE))
        ).text
        assert actual_payment_info == expected_payment_info, f"Expected payment info '{expected_payment_info}', but got '{actual_payment_info}'"
        print(f"Payment information verified as: {actual_payment_info}")

    def click_cancel(self):
        print("Clicking 'Cancel' button...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((CheckoutLocators.CANCEL_BUTTON))
        ).click()
        print("'Cancel' button clicked...")
        print("Verifying navigated back to Cart Page...")
        assert WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CartLocators.CART_TITLE))
        ).text == "Your Cart"
        print("Navigated back to Cart Page verified with title: " + str(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CartLocators.CART_TITLE))
        ).text))

    def click_finish_and_verify_complete(self):
        print("Clicking 'Finish' button...")
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((CheckoutLocators.FINISH_BUTTON))
        ).click()
        print("'Finish' button clicked...")
        print("Verifying navigated to Checkout Complete Page...")
        actual_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((CheckoutLocators.CHECKOUT_COMPLETE_TITLE))
        ).text
        print(f"Actual checkout complete page title: '{actual_title}'")
        assert actual_title == "Thank you for your order!", f"Expected title 'THANK YOU FOR YOUR ORDER', but got '{actual_title}'"
        print("Navigated to Checkout Complete Page verified with title: " + str(actual_title))