from appium import webdriver
import test.functional.android.desired_capabilities as desired_capabilities
import unittest


class BaseSpecification(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('android-automation.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
