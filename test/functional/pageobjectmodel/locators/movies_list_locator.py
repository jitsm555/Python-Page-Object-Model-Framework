from selenium.webdriver.common.by import By

"""
This class contains all common ID's of main movies list page, with these id's we are executing tests 

"""


class MoviesListLocator:
    """ It contains all locators related to movies list"""
    LIST_ID = (By.ID, 'recycler_view')
    TITLE_ID = (By.ID, 'title')
    GENRE_ID = (By.ID, 'genre')
    YEAR_ID = (By.ID, 'year')
