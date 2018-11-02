import os


# Returns abs path relative to this file and not cwd
def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


'''
Get the desired capabilities to start the automation which include
1. platformName
2. platformVersion
3. deviceName :  On Android this capability is currently ignored, though it remains required.
4. app: app=PATH('../../apps/' + app)

    if you don't have apk of application then provide appPackage and appActivity

5. appPackage 
6. appActivity


'''


def get_desired_capabilities(app):
    return dict(platformName='Android', deviceName='Galaxy Tab S3', appPackage='com.medtronic.neuro.dbs.clinician',
                appActivity='.application.lifecycle.activities.StartAppActivity', newCommandTimeout=240)
