from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote import errorhandler

from webdriver.util import NoSuchContextException


class MobileErrorHandler(errorhandler.ErrorHandler):
    def check_response(self, response):
        try:
            super(MobileErrorHandler, self).check_response(response)
        except WebDriverException as wde:
            if wde.msg == 'No such context found.':
                raise NoSuchContextException(wde.msg, wde.screen, wde.stacktrace)
            else:
                raise wde

