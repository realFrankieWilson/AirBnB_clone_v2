#!/usr/bin/python3
"""
script based on the file 1-pack_web_static.py
"""
from fabric.api import *

# Servers to log in to
env.hosts = ['18.207.142.8', '52.86.87.208']
env.user = 'ubuntu'


def do_clean(number=0):
    """ Dlelets contents."""
    number = int(number)

    if number == 0 or number == 1:
        local('cd versions; ls | head -n -1 | xargs rm -fr')
        run('cd /data/web_static/releases ; ls | head -n -1 | xargs rm -rf')
    else:
        local('cd versions; ls | head -n -{} | xargs rm -rf'.format(number))
        run('cd /data/web_static/releases ; ls | head -n -2 | xargs rm -rf'\
                .format(number))
