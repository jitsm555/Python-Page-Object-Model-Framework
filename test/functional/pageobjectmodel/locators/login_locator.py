from selenium.webdriver.common.by import By


class LoginLocators:
    """ It contains all locators related to login page"""
    EMAIL_ID = (By.ID, 'email')
    PASSWORD_ID = (By.ID, 'password')
    SIGN_IN_ID = (By.ID, 'email_sign_in_button')
