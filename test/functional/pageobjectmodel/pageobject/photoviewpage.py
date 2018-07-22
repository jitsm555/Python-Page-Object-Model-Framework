from test.functional.pageobjectmodel.locators.photo_viewer_locator import PhotoViewerLocator
from test.functional.pageobjectmodel.pageobject.basepage import BasePage


class PhotoViewer(BasePage):
    def zoom_photo(driver):
        BasePage.zoom1(PhotoViewerLocator.PHOTO_VIEW_ID, driver)
