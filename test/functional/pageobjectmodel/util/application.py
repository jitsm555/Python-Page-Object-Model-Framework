from test.functional.pageobjectmodel.pageobject.login import Login
from test.functional.pageobjectmodel.pageobject.movieslistpage import MoviesList
from test.functional.pageobjectmodel.pageobject.photoviewpage import PhotoViewer
from test.functional.pageobjectmodel.pageobject.mainactivity import MainActivity
from test.functional.pageobjectmodel.pageobject.viewpagerpage import ViewPager


class Application:
    def __init__(self, driver):
        self.main_activity = MainActivity(driver)
        self.login = Login(driver)
        self.movies_list = MoviesList(driver)
        self.photo_viewer = PhotoViewer(driver)
        self.view_pager = ViewPager(driver)
