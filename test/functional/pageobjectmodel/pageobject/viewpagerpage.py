from test.functional.pageobjectmodel.pageobject import *

"""
This class contains all common method which we will require while executing view pager test
"""


class ViewPager(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_page(self):
        self.swipe()
