# checkout_locators.py
from selenium.webdriver.common.by import By

############## CHECKOUT LOCATORS ##############
class CheckoutLocators:
    CHECKOUT_TITLE = (By.XPATH, '//span[@data-test="title"]')

    # Your Info Form Fields
    FIRST_NAME_FIELD = (By.XPATH, '//input[@data-test="firstName"]')
    LAST_NAME_FIELD = (By.XPATH, '//input[@data-test="lastName"]')
    POSTAL_CODE_FIELD = (By.XPATH, '//input[@data-test="postalCode"]')


    # Checkout Overview Fields
    PAYMENT_INFORMATION_LABEL = (By.XPATH, '//div[@data-test="payment-info-label"]')
    PAYMENT_INFORMATION_VALUE = (By.XPATH, '//div[@data-test="payment-info-value"]')
    SHIPPING_INFORMATION_LABEL = (By.XPATH, '//div[@data-test="shipping-info-label"]')
    SHIPPING_INFORMATION_VALUE = (By.XPATH, '//div[@data-test="shipping-info-value"]')

    PRICE_TOTAL_LABEL = (By.XPATH, '//div[@data-test="total-info-label"]')
    SUBTOTAL_LABEL = (By.XPATH, '//div[@data-test="subtotal-label"]')
    TAX_LABEL = (By.XPATH, '//div[@data-test="tax-label"]')
    TOTAL_LABEL = (By.XPATH, '//div[@data-test="total-label"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@data-test="continue"]')

    # Cancel and Finish Buttons
    CANCEL_BUTTON = (By.XPATH, '//button[@data-test="cancel"]')
    FINISH_BUTTON = (By.XPATH, '//button[@data-test="finish"]')


    # Checkout Complete Fields
    CHECKOUT_COMPLETE_TITLE = (By.XPATH, '//h2[@data-test="complete-header"]')
    CHECKOUT_COMPLETE_TEXT = (By.XPATH, '//div[@data-test="complete-text"]')
    BACK_HOME_BUTTON = (By.XPATH, '//button[@data-test="back-to-products"]')    
