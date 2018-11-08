import unittest
from time import sleep

import desired_capabilities
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from webdriver.util import MultiAction

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1

"""
TODO: In-Progress, Refer page object model
"""


class MultiActionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_parallel_actions(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = self.driver.find_element_by_name('Expandable Lists')
        # simulate a swipe/scroll
        action.press(el).move_to(x=100, y=-1000).release().perform()

        el = self.driver.find_element_by_name('Splitting Touches across Views')
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.ListView')
        a1 = TouchAction()
        a1.press(els[0]) \
            .move_to(x=10, y=0).move_to(x=10, y=-75).move_to(x=10, y=-600).release()

        a2 = TouchAction()
        a2.press(els[1]) \
            .move_to(x=10, y=10).move_to(x=10, y=-300).move_to(x=10, y=-600).release()

        ma = MultiAction(self.driver, els[0])
        ma.add(a1, a2)
        ma.perform()

    def test_actions_with_waits(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        el = self.driver.find_element_by_name('Expandable Lists')
        # simulate a swipe/scroll
        action.press(el).move_to(x=100, y=-1000).release().perform()

        el = self.driver.find_element_by_name('Splitting Touches across Views')
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.ListView')
        a1 = TouchAction()
        a1.press(els[0]) \
            .move_to(x=10, y=0) \
            .move_to(x=10, y=-75) \
            .wait(1000) \
            .move_to(x=10, y=-600) \
            .release()

        a2 = TouchAction()
        a2.press(els[1]) \
            .move_to(x=10, y=10) \
            .move_to(x=10, y=-300) \
            .wait(500) \
            .move_to(x=10, y=-600) \
            .release()

        ma = MultiAction(self.driver, els[0])
        ma.add(a1, a2)
        ma.perform()

    def test_driver_multi_tap(self):
        el = self.driver.find_element_by_name('Graphics')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.driver.scroll(els[len(els) - 1], els[0])

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        if els[len(els) - 1].get_attribute('name') != 'Xfermodes':
            self.driver.scroll(els[len(els) - 1], els[0])

        el = self.driver.find_element_by_name('Touch Paint')
        action.tap(el).perform()

        positions = [(100, 200), (100, 400)]

        # makes two dots in the paint program
        # THE TEST MUST BE WATCHED TO CHECK IF IT WORKS
        self.driver.tap(positions)
        sleep(10)

    def test_driver_pinch(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.driver.scroll(els[len(els) - 1], els[0])

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        if els[len(els) - 1].get_attribute('name') != 'WebView':
            self.driver.scroll(els[len(els) - 1], els[0])

        el = self.driver.find_element_by_name('WebView')
        action.tap(el).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_id('com.example.android.apis:id/wv1')
        self.driver.pinch(element=el)

    def test_driver_zoom(self):
        el1 = self.driver.find_element_by_name('Content')
        el2 = self.driver.find_element_by_name('Animation')
        self.driver.scroll(el1, el2)

        el = self.driver.find_element_by_name('Views')
        action = TouchAction(self.driver)
        action.tap(el).perform()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.driver.scroll(els[len(els) - 1], els[0])

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        if els[len(els) - 1].get_attribute('name') != 'WebView':
            self.driver.scroll(els[len(els) - 1], els[0])

        el = self.driver.find_element_by_name('WebView')
        action.tap(el).perform()

        sleep(SLEEPY_TIME)
        el = self.driver.find_element_by_id('com.example.android.apis:id/wv1')
        self.driver.zoom(element=el)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
