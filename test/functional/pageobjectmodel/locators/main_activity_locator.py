from selenium.webdriver.common.by import By

"""
This class contains all common ID's of main activity page, with these id's we are executing tests 

"""


class MainActivityLocators:
    """ It contains all locators related to login page"""
    LOGIN_ID = (By.ID, 'loginButton')
    MOVIES_LIST_ID = (By.ID, 'movieListButton')
    PHOTO_VIEWER_ID = (By.ID, 'photoViewerButton')
    VIEW_PAGER_ID = (By.ID, 'viewPagerButton')
