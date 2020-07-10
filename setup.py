# coding:utf-8

from setuptools import setup, find_packages

import sys
import os

__version__ = '0.1.2.5'

# or
# from distutils.core import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Thank you for installing stuoe
try:
    print('Thank you for installing stuoe🎵🎵🎵')
    print('')
except:
    # In Python 2.X
    pass

setup(
    name='stuoe',
    version='0.1.2.5',
    description='Lightweight forum, simple interface, easy to install',
    author='snbck',
    author_email='snbckcode@gmail.com',
    url='https://stuoe.cn',
    packages=find_packages(),
        long_description=open('README.md', 'r', encoding="utf-8").read(),
    package_dir={'stuoe': 'stuoe'},
    entry_points={
            'console_scripts': [
                'stuoe=stuoe:cli'
            ]},
    install_requires=['easygui==0.98.1', 'Flask==1.1.2', 'Flask-Avatars==0.2.2', 'Flask-Dropzone==1.5.4', 'Flask-Login==0.5.0', 'Flask-Mail==0.9.1',
                      'Flask-Moment==0.9.0', 'Flask-SQLAlchemy==2.4.1', 'flask-whooshee==0.7.0', 'Flask-WTF==0.14.3', 'gunicorn==20.0.4', 'gevent==20.6.2'],
    include_package_data=True,
    zip_safe=False,
    long_description_content_type="text/markdown",

)

'''
--------------------------

远赴人间惊鸿宴，一睹人间盛世颜

--------------------------
'''
