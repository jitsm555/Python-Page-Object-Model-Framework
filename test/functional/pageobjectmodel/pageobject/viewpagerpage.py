from test.functional.pageobjectmodel.locators.viewpagerlocator import ViewPagerLocator
from test.functional.pageobjectmodel.pageobject import *


class ViewPager(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_to_page(self):
        self.swipe()
