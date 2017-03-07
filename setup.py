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
from setuptools import setup

setup(
    install_requires = [
        'invoke'
    ],
    setup_requires = ['pytest-runner'],
    extras_require = {
        'dev': [
            'flake8',
            'Sphinx',
            'pytest'
        ]
    }
)
