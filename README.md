Python-Page-Object-Model-Framework
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

# Page Object Model 

Page Object Model is a design pattern which has become popular in test automation for enhancing test maintenance 
and reducing code duplication. A page object is an object-oriented class that serves as 
an interface to a page of your AUT.

# Usage
We integrated all Selenium upgraded changes, which makes mobile testing easier in python. We are using appium driver to make remote connection. Please refer below code.  
```python
# Android environment

import test.functional.pageobjectmodel.util.desired_capabilities as desired_capabilities
class BaseSpecification(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('android-automation.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
        

# Returns abs path relative to this file and not cwd
def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


def get_desired_capabilities(app):
    return dict(platformName='Android', deviceName='Galaxy Tab S3',
                app=PATH('../../../apps/' + app), appPackage='com.jiteshmohite619.androidautomation',
                appActivity='.MainActivity', newCommandTimeout=240)
        

```

#### `driver.swipe`

Swipe from one point to another point.

#### `driver.zoom`

Zoom in on an element, doing a pinch out operation.

#### `driver.pinch`

Zoom out on an element, doing a pinch in operation.


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


#### Resetting an application


To reset the running application, use `driver.reset`.

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

#### Shake the device

To shake the device, use `driver.shake`.

```
