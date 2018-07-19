from selenium.webdriver.common.by import By


class MobileBy(By):
    IOS_PREDICATE = '-ios predicate string'
    IOS_UIAUTOMATION = '-ios uiautomation'
    IOS_CLASS_CHAIN = '-ios class chain'
    ANDROID_UIAUTOMATOR = '-android uiautomator'
    ACCESSIBILITY_ID = 'accessibility id'
    IMAGE = '-image'
