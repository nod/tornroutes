#!/usr/bin/env python

from distutils.core import setup

VERSION = open('VERSION').read().lstrip('version: ').rstrip('\n')

setup(
    name = 'tornroutes',
    version = VERSION,
    description = 'Tornado Web Route Decorator',
    author = 'Jeremy Kelley',
    author_email = 'jeremy@33ad.org',
    url = 'https://github.com/nod/tornroutes',
    license = "http://www.apache.org/licenses/LICENSE-2.0",
    packages = ['tornroutes'],
    package_dir={'mypkg': 'src/mypkg'},
    install_requires = ['tornado',]
    )

