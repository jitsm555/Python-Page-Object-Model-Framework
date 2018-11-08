from distutils.core import setup
from setuptools import setup

setup(
    name='Appium-Python-Client',
    version='0.26',
    description='Python client for Appium 1.5',
    keywords=[
        'appium',
        'appium 1.0',
        'selenium',
        'selenium 3',
        'python client',
        'mobile automation'
    ],
    author='Isaac Murchie',
    author_email='isaac@saucelabs.com',
    url='http://appium.io/',
    packages=[
        'appium',
        'appium.common',
        'appium.webdriver',
        'appium.webdriver.common'
    ],
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=['selenium>=2.47.0']
)
