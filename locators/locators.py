# locators.py
from selenium.webdriver.common.by import By

############## BASE LOCATORS ##############
class BasePageLocators:
    TITLE = 'Swag Labs'
    HAMBURGER_MENU = (By.XPATH, '//button[@id="react-burger-btn"]')
    SHOPPING_CART = (By.XPATH, '//a[@data-test="shopping-cart-link"]')
    PRODUCT_FILTER = (By.XPATH, '//select[@data-test="product-sort-container"]')


class BaseModalLocators:
    MODALTITLE = (By.XPATH, "//h5[contains(@class, 'modal-title')]")

