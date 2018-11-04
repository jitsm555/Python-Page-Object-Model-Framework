from test.functional.pageobjectmodel.locators.movies_list_locator import MoviesListLocator
from test.functional.pageobjectmodel.pageobject import *


class MoviesList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll(self):
        self.move_to(MoviesListLocator.LIST_ID)
