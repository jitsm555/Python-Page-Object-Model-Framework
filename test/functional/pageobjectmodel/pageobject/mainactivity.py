from test.functional.pageobjectmodel.locators.main_activity_locator import MainActivityLocators
from test.functional.pageobjectmodel.pageobject.basepage import BasePage


class MainActivity(BasePage):
    def go_to_login(driver):
        return BasePage.click(MainActivityLocators.LOGIN_ID, driver)

    def go_to_movies_list(driver):
        return BasePage.click(MainActivityLocators.MOVIES_LIST_ID, driver)

    def go_to_photo_viewer(driver):
        return BasePage.click(MainActivityLocators.PHOTO_VIEWER_ID, driver)
