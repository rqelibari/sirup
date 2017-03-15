#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    test_basic_data.py - Check if basic data is on specified format.
    Part of sirup test project

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

import sirup
import re


def test_versionInfoIsExposed():
    assert hasattr(sirup, '__version_info__')


def test_versionInfoIsASemanticVersionTuple():
    ver = sirup.__version_info__
    assert isinstance(ver, tuple)
    assert len(ver) == 3
    assert all(isinstance(x, int) for x in ver)


def test_versionIsExposed():
    assert hasattr(sirup, '__version__')


def test_versionIsASemanticVersionString():
    ver = sirup.__version__
    assert isinstance(ver, str)
    assert re.match(r'\d+\.\d+\.\d+', ver)


def test_versionLooksGeneratedFromVersionInfo():
    ver_part = sirup.__version__.split('.')[0]
    ver_info_part = sirup.__version_info__[0]
    assert ver_part == str(ver_info_part)
