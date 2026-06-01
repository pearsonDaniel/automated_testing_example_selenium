# test_remove_from_cart.py
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.login_locators import LoginPageLocators
from locators.homepage_locators import HomePageLocators
import time
import pytest
import requests


@pytest.mark.selenium
def test_remove_from_cart(config_browser, base_url):
        # Initialize the WebDriver and navigate to the login page
        driver = config_browser
        driver.get(base_url)
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
        # Add another item to the cart and verify it was added successfully by checking the button text changes to "Remove"
        home_page.add_item(HomePageLocators.ADD_BIKE_LIGHT_BUTTON, HomePageLocators.REMOVE_BIKE_LIGHT_BUTTON)
        # Remove an item from the cart and verify it was removed successfully by checking the button text changes to "Add to cart"
        home_page.remove_item(HomePageLocators.REMOVE_BACKPACK_BUTTON, HomePageLocators.ADD_BACKPACK_BUTTON)
        # Remove another item from the cart and verify it was removed successfully by checking the button text changes to "Add to cart"
        home_page.remove_item(HomePageLocators.REMOVE_BIKE_LIGHT_BUTTON, HomePageLocators.ADD_BIKE_LIGHT_BUTTON)
        print("***PASS: Items removed from cart successfully***")
        print("###########################################################")