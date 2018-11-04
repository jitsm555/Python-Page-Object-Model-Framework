from selenium.webdriver.common.by import By


class MainActivityLocators:
    """ It contains all locators related to login page"""
    LOGIN_ID = (By.ID, 'loginButton')
    MOVIES_LIST_ID = (By.ID, 'movieListButton')
    PHOTO_VIEWER_ID = (By.ID, 'photoViewerButton')
    VIEW_PAGER_ID = (By.ID, 'viewPagerButton')
