from test.functional.pageobjectmodel.util.wait import WaitForElement

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
