#!/usr/bin/env python
from __future__ import print_function
from sys import argv
from time import sleep

from daemonize import Daemonize

pid = argv[1]
log = argv[2]


def main(a, b, c, language=None, debug=False):
    with open(log, "w") as fp:
        print(a, file=fp)
        print(b, file=fp)
        print(c, file=fp)
        print(language, file=fp)
        print(debug, file=fp)
    while True:
        sleep(5)

daemon = Daemonize(app="test_app", pid=pid, action=main,
                   action_args=("a", "b", "c"),
                   action_kwargs={"language": "Python"})
daemon.start()
