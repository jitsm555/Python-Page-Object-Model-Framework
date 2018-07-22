from test.functional.pageobjectmodel.locators.movies_list_locator import MoviesListLocator
from test.functional.pageobjectmodel.pageobject.basepage import BasePage


class MoviesList(BasePage):
    def scroll(driver):
        BasePage.move_to(MoviesListLocator.LIST_ID, driver)
