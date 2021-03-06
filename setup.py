#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='cryptoaddress',
    version='0.3.6',
    license='GPL',
    description='generate, validate, convert and detect addresses from different crypto currencies.',
    author='peterr',
    author_email='coderiot@zoho.com',
    url='https://github.com/coderiot/cryptoaddress/',
    install_requires=['ecdsa >= 0.10'],
    packages=['address'],
)
