Sirup
=====

.. image:: https://travis-ci.org/rqelibari/sirup.svg?branch=master
    :target: https://travis-ci.org/rqelibari/sirup
    :alt: Code Integration Status on UNIX/Linux

.. image:: https://ci.appveyor.com/api/projects/status/cumkt0u3ya0uky62/branch/master?svg=true
    :target: https://ci.appveyor.com/project/rqelibari/sirup
    :alt: Code Integration Status on Windows

.. image:: https://codecov.io/gh/rqelibari/sirup/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/rqelibari/sirup
    :alt: Code Coverage Status

.. image:: https://readthedocs.org/projects/sirup/badge/?version=latest
    :target: http://sirup.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Sirup is a Python (3.6+) task execution tool, build upon `Invoke`_. It
automates my `MBP`_ setup, configuration and management.

Based on Invoke
-------------------

`Invoke`_ is a great tool and life enhancer! Being still in its
prerelease phase, it is already usable! In the end it will be part of
`Fabric v.2`_, the successor of `Fabric v.1.x`_. For my pourposes it has
everything, is clean, simple and well documentated.

Roadmap
-------

Upnext:

* Configure system settings like Finder, MagicTrackpad and
  Screensaver.
* Install and configure `Homebrew`_ and `Homebrew Cask`_ -
* Install VLC and configure support for BluRays.

Why not Ansible?
----------------

This project is a conclusion after having used `Ansible`_ before. See my
`ansible-osx-playbooks`_ repository on github for more information on
that one. `Ansible`_ has a lot of so called modules, but fails to unify
the interface between the different operating systems (see the ACL
module for example, which does not support NFS v.4 ACLs). As such
ansible just became a more complex way of executing shell commands in my
case. But I liked the idea behind ansible and didn’t want to give up, so
I looked into module development, but found a lot of other flaws there,
too. Because of its encapsulation logic, there is currently no way to
prevent code duplication throughout modules (take a look at `this Google
Groups discussion`_, where Michael DeHaan - the guy who started ansible
- is talking about that). With `Invoke`_ on the other side all those
flaws are gonne (respectively never existed).

.. _Invoke: http://www.pyinvoke.org
.. _MBP: http://www.apple.com/macbook-pro/
.. _Fabric v.2: http://docs.fabfile.org/en/latest/
.. _Fabric v.1.x: http://docs.fabfile.org/en/latest/
.. _Homebrew: http://brew.sh
.. _Homebrew Cask: https://caskroom.github.io
.. _Ansible: http://docs.ansible.com/ansible/index.html
.. _ansible-osx-playbooks: https://github.com/rqelibari/ansible-osx-playbooks
.. _this Google Groups discussion: https://groups.google.com/forum/#!topic/ansible-project/o6WDQ6AdwaUa
