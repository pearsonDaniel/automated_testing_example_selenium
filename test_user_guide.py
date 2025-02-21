# # test_login.py
# from selenium import webdriver
# from src.pages.login_page import LoginPage
# from src.pages.home_page import HomePage
# from locators.locators import *
# import time
# import pytest

# @pytest.mark.selenium
# def test_user_guide():
#     # Initialize the WebDriver
#     driver = webdriver.Chrome()
#     # Open the homepage
#     driver.get(BasePageLocators.BASE_URL)
#     time.sleep(3)
#     login_page = LoginPage(driver)
#     login_page.verify_page_http_200_response(LoginPageLocators.URL)
#     time.sleep(2)
#     login_page.login()
#     login_page.verify_title()
#     home_page = HomePage(driver)
#     time.sleep(3)
#     # Close the WebDriver
#     driver.quit()
