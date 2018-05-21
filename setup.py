# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:54:20 2018

@author: johnc
"""

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)