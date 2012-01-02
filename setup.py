#!/usr/bin/env python

from distutils.core import setup

VERSION = open('VERSION').read().lstrip('version: ').rstrip('\n')

setup(
    version=VERSION,
    name='tornroutes',
    description='Tornado Web Route Decorator',
    author='Jeremy Kelley',
    author_email='jeremy@33ad.org',
    url='https://github.com/nod/tornroutes',
    packages=['tornroutes'],
    package_dir={'tornroutes': 'src/tornroutes'},
    )

