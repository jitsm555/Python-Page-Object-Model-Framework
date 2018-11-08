from test.functional.pageobjectmodel.locators.photo_viewer_locator import PhotoViewerLocator
from test.functional.pageobjectmodel.pageobject import *

"""
This class contains all common method which we will require while executing photo viewer test
"""


class PhotoViewer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def zoom_photo(self):
        self.zoom_view(PhotoViewerLocator.PHOTO_VIEW_ID)
