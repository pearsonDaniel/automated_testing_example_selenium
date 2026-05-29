# test_google_search.py
from conftest import config_browser
from conftest import Config
import time
import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.selenium
def test_google_search(config_browser):
        # Initialize the WebDriver and navigate to the Google homepage
        print("Initializing Webdriver...")
        driver = config_browser
        print("Navigating to Google homepage...")
        driver.get("https://www.google.com/")
        # Verify the Google homepage loads successfully by checking the page title and URL
        print("Verifying Google homepage...")
        assert driver.title == "Google"
        print("Google homepage loaded successfully with title: " + driver.title)
        # Enter a search query into the search field and submit the search
        print("Targeting search box and entering search query...")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python\n")  # '\n' submits the search
        # Wait for the search results to load and verify that the results page is displayed
        print("Waiting for search results to load...")
        time.sleep(2)
        FIRST_ORGANIC_RESULT = (By.CSS_SELECTOR, "h3.LC20lb")
        first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(FIRST_ORGANIC_RESULT)
        )
        print("Clicking on the first search result...")
        first_result.click()
        # Wait for the page to load and verify that the URL of the first search result is correct
        print("Waiting for the page to load...")
        time.sleep(2)
        expected_url = "https://selenium-python.readthedocs.io/"
        print("Verifying the URL of the first search result...")
        assert driver.current_url == expected_url
        print("***PASS: Google search test completed successfully***")
        print("###########################################################")