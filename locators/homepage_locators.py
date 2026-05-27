# homepage_locators.py
from selenium.webdriver.common.by import By

class HomePageLocators:
    URL = 'https://www.saucedemo.com/inventory.html'
    INVENTORY_CONTAINER = (By.XPATH, '//div[@data-test="inventory_container"]')


    # Add to Cart Buttons for Inventory Items
    ADD_BACKPACK_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    ADD_BIKE_LIGHT_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]') 
    ADD_BOLT_TSHIRT_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    ADD_FLEECE_JACKET_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-fleece-jacket"]')
    ADD_ONESIE_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-onesie"]')
    ADD_TEST_ALLTHEITEMS_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

    # Remove from Cart Buttons for Inventory Items
    REMOVE_BACKPACK_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    REMOVE_BIKE_LIGHT_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-bike-light"]')
    REMOVE_BOLT_TSHIRT_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-bolt-t-shirt"]')
    REMOVE_FLEECE_JACKET_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-fleece-jacket"]')
    REMOVE_ONESIE_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-onesie"]')
    REMOVE_TEST_ALLTHEITEMS_BUTTON = (By.XPATH, '//button[@data-test="remove-test.allthethings()-t-shirt-(red)"]')


    # Item titles for Inventory Items
    BACKPACK_TITLE = (By.XPATH, '//a[@data-test="item-4-title-link"]')
    BIKE_LIGHT_TITLE = (By.XPATH, '//a[@data-test="item-0-title-link"]')
    BOLT_TSHIRT_TITLE = (By.XPATH, '//a[@data-test="item-1-title-link"]')
    FLEECE_JACKET_TITLE = (By.XPATH, '//a[@data-test="item-5-title-link"]')
    ONESIE_TITLE = (By.XPATH, '//a[@data-test="item-2-title-link"]')
    TEST_ALLTHEITEMS_TITLE = (By.XPATH, '//a[@data-test="item-3-title-link"]')



    #Item description and price for Inventory Items (General locators, must target individual elements using indexing)
    ITEM_DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')