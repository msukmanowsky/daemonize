#!/usr/bin/env python
from __future__ import print_function
from sys import argv
from time import sleep

from daemonize import Daemonize

pid = argv[1]
log = argv[2]


def privileged_action():
    return ("x", "y", "z")


def main(x, y, z, a, b, c, language=None, debug=False):
    with open(log, "w") as fp:
        print(x, file=fp)
        print(y, file=fp)
        print(z, file=fp)
        print(a, file=fp)
        print(b, file=fp)
        print(c, file=fp)
        print(language, file=fp)
        print(debug, file=fp)
    while True:
        sleep(5)

daemon = Daemonize(app="test_app", pid=pid, action=main,
                   action_args=("a", "b", "c"),
                   action_kwargs={"language": "Python"},
                   privileged_action=privileged_action)
daemon.start()
