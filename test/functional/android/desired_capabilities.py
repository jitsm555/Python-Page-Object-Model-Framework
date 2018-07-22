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
3. deviceName
4. app

'''


def get_desired_capabilities(app):
    return dict(platformName='Android', deviceName='Galaxy Tab S3', app=PATH('../../apps/' + app),
                newCommandTimeout=240)
