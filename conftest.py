# config.py
from selenium import webdriver
import os
import platform

def pytest_addoption(parser):
     parser.addoption(
         "--browser",                  # The custom option
         action="store",           # Stores the value provided
         default="Chrome",            # Default value if not provided
         help="Specify the browser: Chrome, Edge, or Firefox"  # Help description
      )

def config_browser(browser_name):
        if browser_name == "Chrome":
            options = webdriver.ChromeOptions()
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser_name + str())
            return webdriver.Chrome(options=options)
        elif browser_name == "Edge":
            options = webdriver.EdgeOptions()
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser_name + str())
            return webdriver.Edge(options=options)
        elif browser_name == "Firefox":
            options = webdriver.FirefoxOptions()
            print("Session User: " + str(os.getlogin()))
            print("OS Name: " + str(platform.system()))
            print("OS Version: " + str(platform.version()))
            print("Browser: " + browser_name + str())
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported.")

        

class Config:
    BASE_URL = 'https://mtt-staging.cldigitalservices.com/'





