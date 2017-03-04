# Sirup
Sirup is a Python (3.6+) task execution tool, build upon [Invoke][1]. It
automates my [MBP][8] setup, configuration and management.

## Extension of Invoke
[Invoke][1] is a great tool and life enhancer! Being still in its prerelease
phase, it is already usable! In the end it will be part of [Fabric v.2][2], the
successor of [Fabric v.1.x][2].
For my pourposes it has everything, is clean, simple and well documentated.

## Roadmap
Upnext:
- Configure system settings like Finder, MagicTrackpad and Screensaver.
- Install and configure [Homebrew][5] and [Homebrew Cask][6]
- Install VLC and configure support for BluRays.

## Why not Ansible?
This project is a conclusion after having used [Ansible][3] before. See my
[ansible-osx-playbooks][7] repository on github for more information on that
one.
[Ansible][3] has a lot of so called modules, but fails to unify the interface
between the different operating systems (see the ACL module for example,
which does not support NFS v.4 ACLs). As such ansible just became a more
complex way of executing shell commands in my case.
But I liked the idea behind ansible and didn't want to give up, so I looked into
module development, but found a lot of other flaws there, too. Because of its
encapsulation logic, there is currently no way to prevent code duplication
throughout modules (take a look at [this Google Groups discussion][4], where
Michael DeHaan - the guy who started ansible - is talking about that).
With [Invoke][1] on the other side all those flaws are gonne (respectively
never existed).


[1]: http://www.pyinvoke.org
[2]: http://docs.fabfile.org/en/latest/
[3]: http://docs.ansible.com/ansible/index.html
[4]: https://groups.google.com/forum/#!topic/ansible-project/o6WDQ6AdwaUa
[5]: http://brew.sh
[6]: https://caskroom.github.io
[7]: https://github.com/rqelibari/ansible-osx-playbooks
[8]: http://www.apple.com/macbook-pro/
