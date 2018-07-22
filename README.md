Python Automation Framework
====================

# Getting the Appium Python client

There are two ways to install and use the Appium Python client.

1. Install from [PyPi](https://pypi.python.org/pypi), as
['Appium-Python-Client'](https://pypi.python.org/pypi/Appium-Python-Client).

    ```shell
    pip install Appium-Python-Client
    ```

2. Install from source via [GitHub](https://github.com/appium/python-client).

    ```shell
    git clone git@github.com:appium/python-client.git
    cd python-client
    python setup.py install
    ```


# Usage
We integrated all Selenium upgraded changes, which makes mobile testing easier in python. We are using appium driver to make remote connection. Please refer below code.  
```python
# Android environment
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = PATH('../../../apps/android-automation.apk')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```

### Switching between 'Native' and 'Webview'

For mobile testing the Selenium methods for switching between windows was previously
commandeered for switching between native applications and webview contexts. Methods
explicitly for this have been added to the Selenium 3 specification, so moving
forward these 'context' methods are to be used.

To get the current context, rather than calling `driver.current_window_handle` you
use

```python
current = driver.current_context
```

The available contexts are not retrieved using `driver.window_handles` but with

```python
driver.contexts
```

Finally, to switch to a new context, rather than `driver.switch_to.window(name)`,
use the comparable context method

```python
context_name = "WEBVIEW_1"
driver.switch_to.context(context_name)
```

### Finding elements by Android UIAutomator search

This allows elements in an Android application to be found using recursive element
search using the UIAutomator library. Adds the methods `driver.find_element_by_android_uiautomator`
and `driver.find_elements_by_android_uiautomator`.

```python
el = self.driver.find_element_by_android_uiautomator('new UiSelector().description("Animation")')
self.assertIsNotNone(el)
```

```python
els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
self.assertIsInstance(els, list)
```
### Finding elements by Accessibility ID

Allows for elements to be found using the "Accessibility ID". The methods take a
string representing the accessibility id or label attached to a given element, e.g., for iOS the accessibility identifier and for Android the content-description. Adds the methods
`driver.find_element_by_accessibility_id` and `find_elements_by_accessibility_id`.

```python
el = self.driver.find_element_by_accessibility_id('Animation')
self.assertIsNotNone(el)
```

```python
els = self.driver.find_elements_by_accessibility_id('Animation')
self.assertIsInstance(els, list)
```


### Touch actions

In order to accommodate mobile touch actions, and touch actions involving
multiple pointers, the Selenium 3.0 draft specifies ["touch gestures"](https://dvcs.w3.org/hg/webdriver/raw-file/tip/webdriver-spec.html#touch-gestures) and ["multi actions"](https://dvcs.w3.org/hg/webdriver/raw-file/tip/webdriver-spec.html#multiactions-1), which build upon the touch actions.

move_to: note that use keyword arguments if no element

The API is built around `TouchAction` objects, which are chains of one or more actions to be performed in a sequence. The actions are:

#### `perform`

The `perform` method sends the chain to the server in order to be enacted. It also empties the action chain, so the object can be reused. It will be at the end of all single action chains, but is unused when writing multi-action chains.

#### `tap`

The `tap` method stands alone, being unable to be chained with other methods. If you need a `tap`-like action that starts a longer chain, use `press`.

It can take either an element with an optional x-y offset, or absolute x-y coordinates for the tap, and an optional count.

```python
el = self.driver.find_element_by_accessibility_id('Animation')
action = TouchAction(self.driver)
action.tap(el).perform()
el = self.driver.find_element_by_accessibility_id('Bouncing Balls')
self.assertIsNotNone(el)
```

#### `press`

#### `long_press`

#### `release`

#### `move_to`

#### `wait`

#### `cancel`


### Multi-touch actions

In addition to chains of actions performed within a single gesture, it is also possible to perform multiple chains at the same time, to simulate multi-finger actions. This is done through building a `MultiAction` object that comprises a number of individual `TouchAction` objects, one for each "finger".

Given two lists next to each other, we can scroll them independently but simultaneously:

```python
els = self.driver.find_elements_by_class_name('listView')
a1 = TouchAction()
a1.press(els[0]) \
    .move_to(x=10, y=0).move_to(x=10, y=-75).move_to(x=10, y=-600).release()

a2 = TouchAction()
a2.press(els[1]) \
    .move_to(x=10, y=10).move_to(x=10, y=-300).move_to(x=10, y=-600).release()

ma = MultiAction(self.driver, els[0])
ma.add(a1, a2)
ma.perform();
```

### Appium-Specific touch actions

There are a small number of operations that mobile testers need to do quite a bit that can be relatively complicated to build using the Touch and Multi-touch Action API.  For these we provide some convenience methods in the Appium client.

#### `driver.tap`

This method, on the WebDriver object, allows for tapping with multiple fingers, simply by passing in an array of x-y coordinates to tap.

```python
el = self.driver.find_element_by_name('Touch Paint')
action.tap(el).perform()

# set up array of two coordinates
positions = []
positions.append((100, 200))
positions.append((100, 400))

self.driver.tap(positions)
```

#### `driver.swipe`

Swipe from one point to another point.

#### `driver.zoom`

Zoom in on an element, doing a pinch out operation.

#### `driver.pinch`

Zoom out on an element, doing a pinch in operation.



### Application management methods

There are times when you want, in your tests, to manage the running application,
such as installing or removing an application, etc.


#### Backgrounding an application

The method `driver.background_app` sends the running application to the background
for the specified amount of time, in seconds. After that time, the application is
brought back to the foreground.

```python
driver.background_app(1)
sleep(2)
el = driver.find_element_by_name('Animation')
assertIsNotNone(el)
```


#### Checking if an application is installed

To check if an application is currently installed on the device, use the `device.is_app_installed`
method. This method takes the bundle id of the application and return `True` or
`False`.

```python
assertFalse(self.driver.is_app_installed('test'))
assertTrue(self.driver.is_app_installed('com.example.android.androidautomation'))
```


#### Installing an application

To install an uninstalled application on the device, use `device.install_app`,
sending in the path to the application file or archive.

```python
assertFalse(driver.is_app_installed('com.example.android.androidautomation'))
driver.install_app('/path/android-automation.apk')
assertTrue(driver.is_app_installed('com.example.android.androidautomation'))
```


#### Removing an application

If you need to remove an application from the device, use `device.remove_app`,
passing in the application id.

```python
assertTrue(driver.is_app_installed('com.example.android.androidautomation'))
driver.remove_app('com.example.android.apis')
assertFalse(driver.is_app_installed('com.example.android.apis'))
```


#### Closing and Launching an application

To launch the application specified in the desired capabilities, call `driver.launch_app`.
Closing that application is initiated by `driver.close_app`

```python
el = driver.find_element_by_name('Animation')
assertIsNotNone(el)
driver.close_app();

try:
    driver.find_element_by_name('Animation')
except Exception as e:
    pass # should not exist

driver.launch_app()
el = driver.find_element_by_name('Animation')
assertIsNotNone(el)
```

#### Resetting an application

To reset the running application, use `driver.reset`.

```python
el = driver.find_element_by_name('App')
el.click()

driver.reset()
sleep(5)

el = driver.find_element_by_name('App')
assertIsNotNone(el)
```


### Other methods


#### Start an arbitrary activity

The `driver.start_activity` method opens arbitrary activities on a device.
If the activity is not part of the application under test, it will also
launch the activity's application.

```python
driver.start_activity('com.example.android.androidautomation', '.LoginActivity')
```


#### Retrieving application strings

The property method `driver.app_strings` returns the application strings from
the application on the device.

```python
strings = driver.app_strings
```


#### Sending a key event to an Android device

The `driver.keyevent` method sends a keycode to the device. The keycodes can be
found [here](http://developer.android.com/reference/android/view/KeyEvent.html).
Android only.

```python
# sending 'Home' key event
driver.press_keycode(3)
```

#### Retrieving the current running package and activity

The property method `driver.current_package` returns the name of the current
package running on the device.

```python
package = driver.current_package
assertEquals('com.example.android.androidautomation', package)
```

The property method `driver.current_activity` returns the name of the current
activity running on the device.

```python
activity = driver.current_activity
assertEquals('.LoginActivity', activity)
```


#### Set a value directly on an element

Sometimes one needs to directly set the value of an element on the device. To do
this, the method `driver.set_value` or `element.set_value` is invoked.

```python
el = driver.find_element_by_class_name('android.widget.EditText')
driver.set_value(el, 'Testing')

text = el.get_attribute('text')
assertEqual('Testing', text)

el.set_value('More testing')
text = el.get_attribute('text')
assertEqual('More testing', text)
```
#### Set a value to edit text

Sometimes one needs to directly set the value of an element on the device. To do
this, the method `driver.set_value` or `element.set_value` is invoked.

```python
el = driver.find_element('editText1') // id of specifed editext
driver.send_keys(el, 'Testing')

text = el.get_attribute('text')
assertEqual('Testing', text)

el.send_keys('More testing')
text = el.get_attribute('text')
assertEqual('More testing', text)
```


#### Shake the device

To shake the device, use `driver.shake`.

```
