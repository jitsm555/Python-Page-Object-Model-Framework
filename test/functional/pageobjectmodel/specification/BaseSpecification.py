import unittest

from appium import webdriver

import test.functional.pageobjectmodel.util.desired_capabilities as desired_capabilities
from test.functional.pageobjectmodel.util.application import Application


class BaseSpecification(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('android-automation.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.app = Application(self.driver)

    def tearDown(self):
        self.driver.quit()
