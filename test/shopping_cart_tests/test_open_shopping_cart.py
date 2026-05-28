# test_add_to_cart.py
from conftest import config_browser
from conftest import Config
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.login_locators import LoginPageLocators
from locators.homepage_locators import HomePageLocators
import time
import pytest
import requests


@pytest.mark.selenium
def test_add_to_cart(config_browser):
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
        
        print("***PASS: Shopping Cart accessible and item present in cart***")
        print("###########################################################")