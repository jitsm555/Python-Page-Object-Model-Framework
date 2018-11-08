from test.functional.pageobjectmodel.locators.login_locator import LoginLocators
from test.functional.pageobjectmodel.pageobject import *

"""
This class contains all common method which we will require while executing login test
"""


class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_email_id(self, email_id):
        self.__set__(LoginLocators.EMAIL_ID, email_id)

    def get_user_name(self):
        return self.__get__(LoginLocators.EMAIL_ID)

    def set_password(self, password):
        self.__set__(LoginLocators.PASSWORD_ID, password)

    def get_password(self):
        return self.__get__(LoginLocators.PASSWORD_ID)

    def is_login_successful(self):
        return self.__get__(LoginLocators.LOGIN_RESULT) == 'Login Successful'

    def sign_in(self):
        return self.click(LoginLocators.SIGN_IN_ID)
