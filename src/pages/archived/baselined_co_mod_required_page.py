# baselined_co_mod_required_page.py
from src.pages.base_page import BasePage
from locators.locators import *
import time


class BaselinedCOMODRequiredPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
