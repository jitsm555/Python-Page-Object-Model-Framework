from selenium.common.exceptions import InvalidSwitchToTargetException


class NoSuchContextException(InvalidSwitchToTargetException):
    """
    Thrown when context target to be switched doesn't exist.

    To find the current set of active contexts, you can get a list
    of the active contexts in the following way:

        print driver.contexts

    """
    pass
