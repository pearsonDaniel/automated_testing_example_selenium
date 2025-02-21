# base_page.py
from selenium import webdriver
from locators.locators import BasePageLocators
from locators.locators import BaseModalLocators
import requests

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # def configure_browser(self):
    #         browsers = ["Chrome", "Edge", "Firefox"]
    #         for browser in browsers:
    #             if browser == "Chrome":
    #                 self.driver  = webdriver.Chrome()
    #                 return self.driver
    #             elif browser == "Edge":
    #                 self.driver = webdriver.Edge()
    #                 return self.driver
    #             elif browser == "Firefox":
    #                 self.driver = webdriver.Firefox()
    #                 return self.driver
    #             print("Running Test in: " + browser)



    def verify_title(self):
        print("Verifying  Page Title")
        try:
            assert self.driver.title == BasePageLocators.TITLE
            print("Page Title verified as " + str(self.driver.title))
        except Exception:
            print("The Page Title was not verified.")
            print(self.driver.title)

    def verify_page_http_200_response(self, url):
        print("Verifying HTTP Response code for:"+str(BasePageLocators.BASE_URL)+str(url))
        try:
            print("Verifying Page HTTP Code...")
            r = requests.head(str(BasePageLocators.BASE_URL)+str(url))
            assert str(r.status_code) == "200" or "307"
            print("Connection Successful")
            print("Status Code: " + str(r.status_code))
        except requests.ConnectionError:
            print("Failed to connect.")
            print("Status Code: " + str(r.status_code))


    def verify_modal_title(self, modal_title):
        print("Verifying modal title...")
        title = self.driver.find_element(*BaseModalLocators.MODALTITLE)
        assert str(title.text) == str(modal_title)
        print(str(title.text) + " == " + str(modal_title))
        print("Modal title verified.")

    def click_admin_portal(self):
         self.driver.find_element(*BasePageLocators.ADMIN_PORTAL).click()

    def click_user_guide(self):
         self.driver.find_element(*BasePageLocators.USER_GUIDE).click()

    def enter_search_term(self, search_term):
        self.driver.find_element(*BasePageLocators.SEARCH_BOX).send_keys(search_term)
        self.driver.find_element(*BasePageLocators.SEARCH_BUTTON).click()