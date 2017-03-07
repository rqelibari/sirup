#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    tasks.py
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

from invoke import Collection, task
from invocations.watch import watch
import pytest


@task(help={
    'module': "Just runs tests/<module>.py.",
    'opts': "Extra flags (comma separated) for the test runner"
})
def test(c, module=None, opts=None):
    """
    Run tests with pytest.
    """
    args = []

    # Turn users options into argument list items
    if opts:
        # Add whitespace to opts
        optsList = opts.split(',')
        optsList = [elem.strip() for elem in optsList]
        args += optsList

    # Run all suits or only a specific one
    if module:
        specific_module = " ./tests/%s.py" % module
        args.append(specific_module)

    pytest.main(args)


@task(name="watch")
def watch_tests(c, module=None, opts=None):
    """
    Watch source tree and test tree for changes, rerunning tests as necessary.
    Honors ``tests.package`` setting re: which source directory to watch for
    changes.
    """
    package = c.config.get('tests', {}).get('package')
    patterns = ['\./tests/']
    if package:
        patterns.append('\./{0}/'.format(package))
    kwargs = {'module': module, 'opts': opts}
    # Kick things off with an initial test (making sure it doesn't exit on its
    # own if tests currently fail)
    c.config.run.warn = True
    test(c, **kwargs)
    # Then watch
    watch(c, test, patterns, ['.*/\..*\.swp'], **kwargs)


@task
def coverage(c, html=True):
    """
    Run tests w/ coverage enabled, optionally generating HTML & opening it.
    :param bool html:
        Whether to generate & open an HTML report. Default: ``True``.
    """
    # Generate actual coverage data. NOTE: this will honor a local .coveragerc
    package = c.config.get('tests', {}).get('package')
    test_opts = "--cov-config=.coveragerc , --cov=%s" % package
    test(c, opts=test_opts)
    if html:
        c.run("coverage html && open htmlcov/index.html")


ns = Collection(
    test, coverage, watch_tests
)
ns.configure({
    'tests': {
        'package': 'sirup',
    },
})
