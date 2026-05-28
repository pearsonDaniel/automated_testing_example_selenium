# cart_locators.py
from selenium.webdriver.common.by import By

############## CART LOCATORS ##############
class CartLocators:
    CART_TITLE = (By.XPATH, '//span[@data-test="title"]')
    QUANTITY_LABEL = (By.XPATH, '//div[@data-test="cart-quantity-label"]')
    DESCRIPTION_LABEL = (By.XPATH, '//div[@data-test="cart-desc-label"]')
    ITEM_QUANTITY = (By.XPATH, '//div[@data-test="item-quantity"]')
    ITEM_DESCRIPTION = (By.XPATH, '//div[@data-test="inventory-item-desc"]')

    # Cart item name and price
    ITEM_NAME = (By.XPATH, '//div[@data-test="inventory-item-name"]')
    ITEM_PRICE = (By.XPATH, '//div[@data-test="inventory-item-price"]')
    
    # Remove Buttons (scoped per item)
    REMOVE_BACKPACK_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    REMOVE_BIKE_LIGHT_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-bike-light"]')
    REMOVE_BOLT_TSHIRT_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-bolt-t-shirt"]')
    REMOVE_FLEECE_JACKET_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-fleece-jacket"]')
    REMOVE_ONESIE_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-onesie"]')
    REMOVE_TEST_ALLTHEITEMS_BUTTON = (By.XPATH, '//button[@data-test="remove-test.allthethings()-t-shirt-(red)"]')


    # Bottom buttons
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//button[@data-test="continue-shopping"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@data-test="checkout"]')

