# test_checkout_shopping_cart.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from locators.login_locators import LoginPageLocators
from locators.homepage_locators import HomePageLocators
from locators.checkout_locators import CheckoutLocators
from locators.cart_locators import CartLocators
import time
import pytest
import requests


@pytest.mark.selenium
def test_checkout_shopping_cart(config_browser):
        # Initialize the WebDriver and navigate to the login page
        driver = config_browser
        driver.get(Config.BASE_URL)
        # Create an instance of the LoginPage and perform login actions
        login_page = LoginPage(driver)
        # Verify the login page loads successfully by checking the page title and URL
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        # Perform login and verify successful login by checking the page title and URL
        login_page.login()
        # After login, create an instance of the HomePage and verify it loads successfully
        home_page = HomePage(driver)
        # Add an item to the cart and verify it was added successfully by checking the button text changes to "Remove"
        home_page.add_item(HomePageLocators.ADD_BACKPACK_BUTTON, HomePageLocators.REMOVE_BACKPACK_BUTTON)
        # Open the Shopping Cart and verify the item is in the cart
        home_page.click_shopping_cart()
        # Verify the item is in the cart by checking the cart item, quantity, and price
        cart_page = CartPage(driver)
        cart_page.verify_item_in_cart(CartLocators.ITEM_NAME, CartLocators.ITEM_QUANTITY, CartLocators.ITEM_PRICE, "Sauce Labs Backpack", 1, "$29.99")
        # Click the 'Checkout' button and verify navigated to Checkout Page
        cart_page.click_checkout()       
        # Instantiate the CheckoutPage to verify the checkout page is loaded successfully by checking the page title and URL
        checkout_page = CheckoutPage(driver)
        # Add Information for Checkout
        checkout_page.add_checkout_info("John", "Doe", "12345")
        checkout_page.click_continue()
        # Verify Payment Info
        checkout_page.verify_payment_info("SauceCard #31337")
        # Click Finish and verify navigated to Checkout Complete Page
        checkout_page.click_finish_and_verify_complete()
        print("***PASS: Shopping Cart accessible and item present in cart***")
        print("###########################################################")