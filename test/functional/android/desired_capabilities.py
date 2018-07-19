import os


# Returns abs path relative to this file and not cwd
def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Galaxy Tab S3',
        'app': PATH('../../apps/' + app),
        'newCommandTimeout': 240
    }

    return desired_caps
