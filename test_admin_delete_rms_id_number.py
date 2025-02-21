# # test_admin_portal.py
# from selenium import webdriver
# from src.pages.login_page import LoginPage
# from src.pages.admin_rms_page import AdminRMSPage
# from locators.locators import *
# import time
# import pytest

# @pytest.mark.selenium
# def test_admin_delete_rms_id_number():

#     browsers = ["Chrome", "Edge", "Firefox"]
#     for browser in browsers:
#         if browser == "Chrome":
#             driver = webdriver.Chrome()
#         elif browser == "Edge":
#             driver = webdriver.Edge()
#         elif browser == "Firefox":
#             driver = webdriver.Firefox()
#         print("Running Test in: " + browser)
#         # Open the homepage
#         driver.get(BasePageLocators.BASE_URL)
#         time.sleep(3)
#         login_page = LoginPage(driver)
#         login_page.verify_page_http_200_response(LoginPageLocators.URL)
#         login_page.verify_title()
#         time.sleep(2)
#         login_page.login()
#         driver.get(BasePageLocators.BASE_URL+AdminRMSLocators.URL)
#         admin_rms_page = AdminRMSPage(driver)
#         admin_rms_page.verify_title()
#         admin_rms_page.verify_page_http_200_response(AdminRMSLocators.URL)
#         admin_rms_page.search_rms_id()
#         if browser == "Firefox":
#             admin_rms_page.delete_rms_id()

#         time.sleep(3)
#         print("###########################################################")

#         # Close the WebDriver
#         driver.quit()
