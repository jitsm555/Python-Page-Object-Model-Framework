from test.functional.pageobjectmodel.util.wait import WaitForElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from time import sleep

'''
Base class will contain all common functionality 
'''


class BasePage:
    """Base page class that is initialized on every page object class."""

    def __set__(locator, driver, value):
        """Set the supplied text to the specified object"""
        WaitForElement.wait(driver, locator)
        element = driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def __get__(locator, driver):
        """Gets the text of the specified object"""
        WaitForElement.wait(driver, locator)
        element = driver.find_element(*locator)
        return element.get_attribute("text")

    def click(locator, driver):
        WaitForElement.wait(driver, locator)
        element = driver.find_element(*locator)
        element.click()

    def move_to(locator, driver):
        WaitForElement.wait(driver, locator)
        action = TouchAction(driver)
        el = driver.find_element(*locator)
        action.press(el).move_to(x=10, y=500).release().perform()

    def zoom1(locator, driver):
        # TODO : code is in progress
        xx = driver.get_window_size()['width'] / 2
        yy = driver.get_window_size()['height'] / 2
        print("akash" + str(xx))
        print("akash1" + str(yy))
        action1 = TouchAction(driver)
        action2 = TouchAction(driver)
        final_action = MultiAction(driver)
        # Pinch
        action1.long_press(x=xx, y=yy - 50).move_to(x=0, y=500).release()
        action2.long_press(x=xx, y=yy + 50).move_to(x=0, y=-500).release()
        final_action.add(action1, action2)
        final_action.perform()
