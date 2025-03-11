# config.py
from selenium import webdriver
import os
import platform


def config_browser(browser):
        if browser == "Chrome":
            options = webdriver.ChromeOptions()
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser + str())
            return webdriver.Chrome(options=options)
        elif browser == "Edge":
            options = webdriver.EdgeOptions()
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser + str())
            return webdriver.Edge(options=options)
        elif browser == "Firefox":
            options = webdriver.FirefoxOptions()
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser + str())
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser '{browser}' is not supported.")

        

class Config:
    BASE_URL = 'https://mtt-staging.cldigitalservices.com/'
