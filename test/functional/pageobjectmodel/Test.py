import unittest

from test.functional.pageobjectmodel.specification.BaseSpecification import BaseSpecification
import time
import pytest

'''
Login credential to do login
'''
EMAIL_ID = 'admin@gmail.com'
PASSWORD = 'admin@123'


# http://selenium-python.readthedocs.io/page-objects.html
# http://selenium-python.readthedocs.io/locating-elements.html
class Test(BaseSpecification):
    @pytest.mark.run(order=1)
    def test_login(self):
        self.app.main_activity.go_to_login()
        self.app.login.set_email_id(EMAIL_ID)
        print(self.app.login.get_user_name())
        self.app.login.set_password(PASSWORD)
        print(self.app.login.get_password())
        self.app.login.sign_in()
        assert self.app.login.is_login_successful()

    @pytest.mark.run(order=2)
    def test_movies_list(self):
        self.app.main_activity.go_to_movies_list()
        self.app.movies_list.scroll()

    @pytest.mark.run(order=3)
    def test_photo_viewer(self):
        self.app.main_activity.go_to_photo_viewer()
        time.sleep(5)
        self.app.photo_viewer.zoom_photo()
        time.sleep(5)

    @pytest.mark.run(order=4)
    def test_view_pager(self):
        self.app.main_activity.go_to_view_pager()
        time.sleep(5)
        self.app.view_pager.navigate_to_page()
        time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
