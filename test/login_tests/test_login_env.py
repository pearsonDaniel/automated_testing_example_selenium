# test_login_env.py
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from locators.login_locators import LoginPageLocators
from locators.homepage_locators import HomePageLocators
import time
import pytest
import requests



@pytest.mark.selenium
def test_login_env(config_browser, base_url):
        # Initialize the WebDriver and navigate to the login page
        driver = config_browser
        driver.get(base_url)
        # Create an instance of the LoginPage and perform login actions
        login_page = LoginPage(driver)
        # Verify the login page loads successfully by checking the page title and URL
        login_page.verify_page_http_200_response(LoginPageLocators.URL)
        # Perform login and verify successful login by checking the page title and URL
        login_page.login_env()
        # After login, create an instance of the HomePage and verify it loads successfully
        home_page = HomePage(driver)
        # Verify the home page loads successfully by checking the page title and URL
        home_page.verify_title()
        print("Current URL: " + str(driver.current_url))
        print("***PASS: Successfully Logged In***")
        print("###########################################################")






