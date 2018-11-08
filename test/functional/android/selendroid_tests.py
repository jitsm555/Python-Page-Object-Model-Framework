import unittest
from time import sleep

import desired_capabilities
from selenium.webdriver.common.touch_actions import TouchActions

from appium import webdriver

"""
TODO: In-Progress, Refer page object model
"""


class SelendroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        desired_caps['automationName'] = 'Selendroid'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_contexts_list(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')
        els = el.find_elements_by_class_name('android.widget.TextView')

        ta = TouchActions(self.driver).flick_element(el, 0, -300, 0)
        ta.perform()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def _enter_webview(self):
        btn = self.driver.find_element_by_name('buttonStartWebviewCD')
        btn.click()
        self.driver.switch_to.context('WEBVIEW')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SelendroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
