import unittest
from test.functional.pageobjectmodel.pageobject.login import Login
from test.functional.pageobjectmodel.support.BaseSpecification import BaseSpecification

EMAIL_ID = 'admin@gmail.com'
PASSWORD = 'admin@123'


# http://selenium-python.readthedocs.io/page-objects.html
# http://selenium-python.readthedocs.io/locating-elements.html
class LoginTest(BaseSpecification):
    def test_login(self):
        driver = self.driver
        Login.set_email_id(driver, EMAIL_ID)
        print(Login.get_user_name(driver))
        Login.set_password(driver, EMAIL_ID)
        print(Login.get_password(driver))
        Login.sign_in(driver)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
