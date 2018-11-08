import os

'''
Get the desired capabilities to start the automation which include
1. platformName 
2. platformVersion
3. deviceName :  On Android this capability is currently ignored, though it remains required.
4. app: app=PATH('../../apps/' + app)

    If you don't have apk of application then provide appPackage and appActivity
5. appPackage 
6. appActivity


'''


# Returns abs path relative to this file and not cwd
def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


def get_desired_capabilities(app):
    return dict(platformName='Android', deviceName='Galaxy Tab S3',
                app=PATH('../../../apps/' + app), appPackage='com.jiteshmohite619.androidautomation',
                appActivity='.MainActivity', newCommandTimeout=240)
