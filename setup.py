#!/usr/bin/env python

from distutils.core import setup

setup(name='tornado_addons',
      version='0.02.1',
      description='Tornado Web Route Decorator',
      author='Jeremy Kelley',
      author_email='jeremy@33ad.org',
      url='https://github.com/nod/tornado_addons',
      packages=['tornroutes'],
      package_dir={'tornroutes':'tornroutes'},
     )

