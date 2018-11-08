import unittest

import desired_capabilities

from appium import webdriver
from webdriver.connectiontype import ConnectionType

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1

"""
TODO: In-Progress, Refer page object model
"""


class NetworkConnectionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_get_network_connection(self):
        nc = self.driver.network_connection
        self.assertIsInstance(nc, int)

    def test_set_network_connection(self):
        nc = self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        self.assertIsInstance(nc, int)
        self.assertEqual(nc, ConnectionType.DATA_ONLY)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(NetworkConnectionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
