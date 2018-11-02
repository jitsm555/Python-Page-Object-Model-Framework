

import unittest

from appium.webdriver.common.touch_action import TouchAction

from webdriver.util import MultiAction


class MultiActionTests(unittest.TestCase):
    def setUp(self):
        self._multi_action = MultiAction(DriverStub())

    def test_json(self):
        self.maxDiff = None
        json = {
            'actions': [
                [
                    {'action': 'press', 'options': {'x': None, 'y': None, 'element': 1}},
                    {'action': 'moveTo', 'options': {'x': 10, 'y': 20}},
                    {'action': 'release', 'options': {}}
                ],
                [
                    {'action': 'press', 'options': {'x': 11, 'y': 30, 'element': 5}},
                    {'action': 'moveTo', 'options': {'x': 12, 'y': -300}},
                    {'action': 'release', 'options': {}}
                ]
            ],
            'elementId': 0
        }
        t1 = TouchAction(DriverStub()).press(ElementStub(1)).move_to(x=10, y=20).release()
        t2 = TouchAction(DriverStub()).press(ElementStub(5), 11, 30).move_to(x=12, y=-300).release()
        self._multi_action.add(t1, t2)
        self.assertEqual(json, self._multi_action.json_wire_gestures)


class DriverStub(object):
    def execute(self, action, params):
        print "driver.execute called"


class ElementStub(object):
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id


if __name__ == "__main__":
    unittest.main()
