from selenium.webdriver.common.by import By

"""
This class contains all common ID's of main photo viewer page, with these id's we are executing tests 

"""


class PhotoViewerLocator:
    """ It contains all locators related to photo view"""
    PHOTO_VIEW_ID = (By.ID, 'photo_view')
