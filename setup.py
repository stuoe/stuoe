# coding:utf-8

from setuptools import setup, find_packages

import sys
import os
import io


__version__ = '0.1.3'

# or
# from distutils.core import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
BASE_DIR = os.path.join(os.path.dirname(__file__))

with io.open(os.path.join(BASE_DIR, 'requirements.txt'), encoding='utf-8') as fh:
    REQUIREMENTS = fh.read()

# Thank you for installing stuoe
try:
    print('Thank you for installing stuoe🎵🎵🎵')
    print('')
except:
    # In Python 2.X
    pass

setup(
    name='stuoe',
    version='0.1.3',
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
    install_requires=REQUIREMENTS,
    include_package_data=True,
    license='Apache License',
    zip_safe=False,
    long_description_content_type="text/markdown",

)

'''
--------------------------

远赴人间惊鸿宴，一睹人间盛世颜

--------------------------
'''
