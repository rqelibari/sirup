#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    setup.py
    Part of sirup project

    (c) 2017 Copyright Rezart Qelibari <rqelibari@users.noreply.github.com>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

# Support setuptools only, distutils has a divergent and more annoying API
from setuptools import setup, find_packages

# Version info -- read without importing
_locals = {}
with open('sirup/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# Frankenstein long_description: version-specific changelog note + README
long_description = """
To find out what's new in this version of Sirup, please see `the changelog
<http://github.com/rqelibari/sirup/changelog.html#%s>`_.

%s
""" % (version, open('README.rst').read())

setup(
    name='sirup',
    version=version,
    description='Pythonic task execution',
    license='BSD',

    long_description=long_description,
    author='Rezart Qelibari',
    author_email='rqelibari@users.noreply.github.com',
    url='https://github.com/rqelibari/sirup',

    packages=find_packages(),
    install_requires=[
        'invoke'
    ],
    setup_requires=['pytest-runner'],
    extras_require={
        'dev': [
            'flake8',
            'Sphinx',
            'pytest'
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],
)
