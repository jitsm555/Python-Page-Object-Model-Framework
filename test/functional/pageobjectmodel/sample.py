import unittest
from test.functional.pageobjectmodel.pageobject.login import Login
from test.functional.pageobjectmodel.pageobject.movieslistpage import MoviesList
from test.functional.pageobjectmodel.pageobject.photoviewpage import PhotoViewer
from test.functional.pageobjectmodel.pageobject.mainactivity import MainActivity
from test.functional.pageobjectmodel.support.BaseSpecification import BaseSpecification

'''
Login credential to do login
'''
EMAIL_ID = 'admin@gmail.com'
PASSWORD = 'admin@123'


# http://selenium-python.readthedocs.io/page-objects.html
# http://selenium-python.readthedocs.io/locating-elements.html
class LoginTest(BaseSpecification):
    def test_login(self):
        driver = self.driver
        MainActivity.go_to_login(driver)
        Login.set_email_id(driver, EMAIL_ID)
        print(Login.get_user_name(driver))
        Login.set_password(driver, PASSWORD)
        print(Login.get_password(driver))
        Login.sign_in(driver)
        assert Login.is_login_successful(driver)

    def test_movies_list(self):
        driver = self.driver
        MainActivity.go_to_movies_list(driver)
        MoviesList.scroll(driver)

    def test_photo_viewer(self):
        driver = self.driver
        MainActivity.go_to_photo_viewer(driver)
        PhotoViewer.zoom_photo(driver)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
