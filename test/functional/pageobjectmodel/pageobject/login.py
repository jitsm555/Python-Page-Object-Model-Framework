from test.functional.pageobjectmodel.locators.login_locator import LoginLocators
from test.functional.pageobjectmodel.pageobject.basepage import BasePage


class Login(BasePage):
    def set_email_id(driver, email_id):
        BasePage.__set__(LoginLocators.EMAIL_ID, driver, email_id)

    @staticmethod
    def get_user_name(driver):
        return BasePage.__get__(LoginLocators.EMAIL_ID, driver)

    def set_password(driver, password):
        BasePage.__set__(LoginLocators.PASSWORD_ID, driver, password)

    @staticmethod
    def get_password(driver):
        return BasePage.__get__(LoginLocators.PASSWORD_ID, driver)

    def sign_in(driver):
        return BasePage.click(LoginLocators.SIGN_IN_ID, driver)
