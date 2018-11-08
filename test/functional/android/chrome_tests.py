import unittest

from appium import webdriver

"""
TODO: In-Progress, Refer page object model
"""


class ChromeTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Galaxy Tab S3',
            'browserName': 'Chrome'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        self.driver.get('http://10.0.2.2:4723/test/guinea-pig')
        self.driver.find_element_by_link_text('i am a link').click()

        self.assertTrue('I am some other page content' in self.driver.page_source)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ChromeTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
