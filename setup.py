#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('README.rst') as readme:
    __doc__ = readme.read()

from setuptools import setup

setup(
    name='pdb4qt',
    version='0.2',
    description=u'A set_trace() that works with PyQt4',
    long_description=__doc__,
    author = u'Martín Gaitán',
    author_email = 'gaitan@gmail.com',
    url='https://github.com/nqnwebs/pdb4qt',
    packages=['pdb4qt'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
      ]
)
