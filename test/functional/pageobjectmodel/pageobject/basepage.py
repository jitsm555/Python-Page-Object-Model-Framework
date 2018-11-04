from appium.webdriver.common.touch_action import TouchAction

from test.functional.pageobjectmodel.util.wait import WaitForElement
from webdriver.util.multi_action import MultiAction

'''
Base class will contain all common functionality 
'''


class BasePage:
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        self.driver = driver

    def __set__(self, locator, value):
        """Set the supplied text to the specified object"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def __get__(self, locator):
        """Gets the text of the specified object"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        return element.get_attribute("text")

    def click(self, locator):
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.click()

    def click_list_item(self, locator, pos):
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_elements(*locator)[pos]
        element.click()

    def click_list_item_by_text(self, locator, text):
        WaitForElement.wait(self.driver, locator)
        for element in self.driver.find_elements(*locator):
            if text == element.text:
                element.click()

    def move_to(self, locator):
        WaitForElement.wait(self.driver, locator)
        action = TouchAction(self.driver)
        el = self.driver.find_element(*locator)
        action.press(el).move_to(x=10, y=500).release().perform()

    def zoom_view(self, locator):
        # TODO : Currently, It is not working
        # xx = driver.get_window_size()['width'] / 2
        # yy = driver.get_window_size()['height'] / 2
        el = self.driver.find_element(*locator)
        x1 = el.location['x']
        y1 = el.location['y']
        #
        x = x1 + el.size['width'] / 2
        y = y1 + el.size['height'] / 2

        action1 = TouchAction(self.driver)
        action2 = TouchAction(self.driver)
        # action1.press(el)
        # action2.press(el)
        final_action = MultiAction(self.driver)
        # # action1.move_to(x=0, y=50).wait(500).release()
        # # action2.move_to(x=0, y=-50).wait(500).release()
        # # Pinch
        action1.long_press(el, x, y - 20).move_to(el, x, y - 2000)
        action2.long_press(el, x, y + 20).move_to(el, x, y + 2000)
        final_action.add(action1, action2)
        final_action.perform()

        # driver.pinch(element=el, percent=150, steps=100)

    def swipe(self):
        self.driver.swipe(475, 500, 75, 500, 400)
