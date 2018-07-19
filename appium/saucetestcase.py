import unittest
import os
import sys
from appium import webdriver
from sauceclient import SauceClient

SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
sauce = SauceClient(SAUCE_USERNAME, SAUCE_ACCESS_KEY)


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            name = "%s_%s" % (base_class.__name__, i + 1)
            d = {'desired_capabilities' : platform}
            module[name] = type(name, (base_class,), d)
    return decorator


class SauceTestCase(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)
    
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

