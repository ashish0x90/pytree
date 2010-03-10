#!/usr/bin/env python

from distutils.core import setup

setup(name='pytree',
      version='1.0',
      description='A Library of various Tree based data structures',
      author='Ashish Yadav',
      author_email='ashish.nopc0de@gmail.com',
      url='http://github.com/ashish0x90/pytree/',
      packages=['pytree'],
      package_dir={
        "pytree" :"src/pytree",
            }
      )
