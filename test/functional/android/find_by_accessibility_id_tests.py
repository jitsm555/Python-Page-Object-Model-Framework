import unittest

from appium import webdriver
import desired_capabilities

"""
TODO: In-Progress, Refer page object model
"""


class FindByAccessibilityIDTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        self.assertIsNotNone(el)

    def test_find_multiple_elements(self):
        els = self.driver.find_elements_by_accessibility_id('Animation')
        self.assertIsInstance(els, list)

    def test_element_find_single_element(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')

        sub_el = el.find_element_by_accessibility_id('Animation')
        self.assertIsNotNone(sub_el)

    def test_element_find_multiple_elements(self):
        el = self.driver.find_element_by_class_name('android.widget.ListView')

        sub_els = el.find_elements_by_accessibility_id('Animation')
        self.assertIsInstance(sub_els, list)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByAccessibilityIDTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
