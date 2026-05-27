# login_locators.py
from selenium.webdriver.common.by import By

class LoginPageLocators:
    URL = 'https://www.saucedemo.com/'
    USERNAME_FIELD = (By.XPATH, '//input[@data-test="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')