from selenium.webdriver.common.by import By


class MobileBy(By):
    ANDROID_UIAUTOMATOR = '-android uiautomator'
    ACCESSIBILITY_ID = 'accessibility id'
    IMAGE = '-image'
