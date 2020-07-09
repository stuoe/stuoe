# coding:utf-8

from setuptools import setup, find_packages

import sys
import os

# or
# from distutils.core import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Thank you for installing stuoe
try:
    print('Thank you for installing stuoe')
    print('')
except:
    # In Python 2.X
    pass

setup(
    name='stuoe',
    version='0.1.1',
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
    include_package_data=True,
    zip_safe=False,

)

'''
--------------------------

远赴人间惊鸿宴，一睹人间盛世颜

--------------------------
'''
