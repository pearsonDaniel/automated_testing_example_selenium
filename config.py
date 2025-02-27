# config.py
from selenium import webdriver
import os

def config_browser(browser_name):
        if browser_name == "Chrome":
            options = webdriver.ChromeOptions()
            print("Session User: " + str(os.getlogin()))
            print("Running Test in: " + browser_name)
            return webdriver.Chrome(options=options)
        elif browser_name == "Edge":
            options = webdriver.EdgeOptions()
            print("Session User: " + str(os.getlogin()))
            print("Running Test in: " + browser_name)
            return webdriver.Edge(options=options)
        elif browser_name == "Firefox":
            options = webdriver.FirefoxOptions()
            print("Session User: " + str(os.getlogin()))
            print("Running Test in: " + browser_name)
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")
        

class Config:
    BASE_URL = 'https://mtt-staging.cldigitalservices.com/'
