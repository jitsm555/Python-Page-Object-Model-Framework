from test.functional.pageobjectmodel.locators.movies_list_locator import MoviesListLocator
from test.functional.pageobjectmodel.pageobject import *

"""
This class contains all common method which we will require while executing movie list test
"""


class MoviesList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll(self):
        self.move_to(MoviesListLocator.LIST_ID)
