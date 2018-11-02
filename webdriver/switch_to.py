from selenium.webdriver.remote.switch_to import SwitchTo

from .mobilecommand import MobileCommand


class MobileSwitchTo(SwitchTo):
    def context(self, context_name):
        """
        Sets the context for the current session.

        :Args:
         - context_name: The name of the context to switch to.

        :Usage:
            driver.switch_to.context('WEBVIEW_1')
        """
        self._driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': context_name})
