#!/usr/bin/env python

from distutils.core import setup

setup(name='tornado_addons',
      version='0.02',
      description='Tornado Web Add-ons',
      author='Jeremy Kelley',
      author_email='jeremy@collectivelabs.com',
      url='https://github.com/nod/tornado_addons',
      packages=['tornado_addons'],
      package_dir={'tornado_addons':'tornado_addons'},
     )

