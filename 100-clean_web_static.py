#!/usr/bin/python3
"""
script based on the file 1-pack_web_static.py
"""
from fabric.api import *
import os

# Servers to log in to
env.hosts = ['18.207.142.8', '52.86.87.208']
env.user = 'ubuntu'


def do_clean(number=0):
    """ Dlelets contents."""
    number = 1 if int(number) == 0 else int(number)

    arch = sorted(os.listdir("versions"))
    [arch.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arch]

    with cd("/data/web_static/releases"):
        arch = run("ls -tr").split()
        arch = [a for a in arch if "web_static_" in a]
        [run("rm -rf ./{}".format(a)) for a in arch]
