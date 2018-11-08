import unittest
from time import sleep

import desired_capabilities
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

from webdriver.util.touch_action import TouchAction

# the emulator is sometimes slow
SLEEPY_TIME = 2

"""
TODO: In-Progress, Refer page object model
"""


class TouchActionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_tap(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.tap(el).perform()
        el = self.driver.find_element_by_accessibility_id('Bouncing Balls')
        self.assertIsNotNone(el)

    def test_tap_x_y(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.tap(el, 100, 10).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_accessibility_id('Bouncing Balls')
        self.assertIsNotNone(el)

    def test_tap_twice(self):
        el = self.driver.find_element_by_name('Text')
        action = TouchAction(self.driver)
        action.tap(el).perform()
        sleep(SLEEPY_TIME)

        el = self.driver.find_element_by_name('LogTextBox')
        action.tap(el).perform()

        el = self.driver.find_element_by_name('Add')
        action.tap(el, count=2).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.assertEqual('This is a test\nThis is a test\n', els[1].get_attribute("text"))

    def test_press_and_immediately_release(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.press(el).release().perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_accessibility_id('Bouncing Balls')
        self.assertIsNotNone(el)

    def test_press_and_immediately_release_x_y(self):
        el = self.driver.find_element_by_accessibility_id('Animation')
        action = TouchAction(self.driver)
        action.press(el, 100, 10).release().perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_accessibility_id('Bouncing Balls')
        self.assertIsNotNone(el)

    def test_press_and_wait(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_accessibility_id('Animation')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_accessibility_id('Views')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_accessibility_id('Expandable Lists')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_accessibility_id('1. Custom Adapter')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_name('People Names')
        # self.assertIsNotNone(el)
        action.press(el).wait(2000).perform()

        sleep(SLEEPY_TIME)
        # 'Sample menu' only comes up with a long press, not a press
        el = self.driver.find_element_by_name('Sample menu')
        self.assertIsNotNone(el)

    def test_press_and_moveto(self):
        el1 = self.driver.find_element_by_accessibility_id('Content')
        el2 = self.driver.find_element_by_accessibility_id('Animation')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2).release().perform()

        el = self.driver.find_element_by_accessibility_id('Views')
        self.assertIsNotNone(el)

    def test_press_and_moveto_x_y(self):
        el1 = self.driver.find_element_by_accessibility_id('Content')
        el2 = self.driver.find_element_by_accessibility_id('App')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2, 100, 100).release().perform()

        el = self.driver.find_element_by_accessibility_id('Views')
        self.assertIsNotNone(el)

    def test_long_press(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_accessibility_id('Animation')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2).perform()

        el = self.driver.find_element_by_accessibility_id('Views')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        el = self.driver.find_element_by_accessibility_id('Expandable Lists')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        el = self.driver.find_element_by_accessibility_id('1. Custom Adapter')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        el = self.driver.find_element_by_name('People Names')
        # self.assertIsNotNone(el)
        action.long_press(el).perform()

        # 'Sample menu' only comes up with a long press, not a tap
        el = self.driver.find_element_by_name('Sample menu')
        self.assertIsNotNone(el)

    def test_long_press_x_y(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_accessibility_id('Animation')

        action = TouchAction(self.driver)
        action.press(el1).move_to(el2).perform()

        el = self.driver.find_element_by_accessibility_id('Views')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        el = self.driver.find_element_by_accessibility_id('Expandable Lists')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        el = self.driver.find_element_by_accessibility_id('1. Custom Adapter')
        # self.assertIsNotNone(el)
        action.tap(el).perform()

        # the element "People Names" is located at 0:110 (top left corner)
        action.long_press(x=10, y=120).perform()

        # 'Sample menu' only comes up with a long press, not a tap
        el = self.driver.find_element_by_name('Sample menu')
        self.assertIsNotNone(el)

    def test_drag_and_drop(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = self.driver.find_element_by_name('Drag and Drop')
        action.tap(el).perform()

        dd3 = self.driver.find_element_by_id('com.example.android.apis:id/drag_dot_3')
        dd2 = self.driver.find_element_by_id('com.example.android.apis:id/drag_dot_2')

        # dnd is stimulated by longpress-move_to-release
        action.long_press(dd3).move_to(dd2).release().perform()

        el = self.driver.find_element_by_id('com.example.android.apis:id/drag_result_text')
        self.assertEqual('Dropped!', el.get_attribute('text'))

    def test_driver_drag_and_drop(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = self.driver.find_element_by_name('Drag and Drop')
        action.tap(el).perform()

        dd3 = self.driver.find_element_by_id('com.example.android.apis:id/drag_dot_3')
        dd2 = self.driver.find_element_by_id('com.example.android.apis:id/drag_dot_2')

        self.driver.drag_and_drop(dd3, dd2)

        el = self.driver.find_element_by_id('com.example.android.apis:id/drag_result_text')
        self.assertEqual('Dropped!', el.get_attribute('text'))

    def test_driver_swipe(self):
        self.assertRaises(NoSuchElementException, self.driver.find_element_by_name, 'Views')

        self.driver.swipe(100, 500, 100, 100, 800)
        el = self.driver.find_element_by_name('Views')
        self.assertIsNotNone(el)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TouchActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
