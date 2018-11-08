from test.functional.pageobjectmodel.locators.main_activity_locator import MainActivityLocators
from test.functional.pageobjectmodel.pageobject import *

"""
This class contains all common method which we will require while executing main activity test
"""


class MainActivity(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_login(self):
        return self.click(MainActivityLocators.LOGIN_ID)

    def go_to_movies_list(self):
        return self.click(MainActivityLocators.MOVIES_LIST_ID)

    def go_to_photo_viewer(self):
        return self.click(MainActivityLocators.PHOTO_VIEWER_ID)

    def go_to_view_pager(self):
        return self.click(MainActivityLocators.VIEW_PAGER_ID)
