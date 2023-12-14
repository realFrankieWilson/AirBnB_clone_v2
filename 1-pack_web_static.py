#!/usr/bin/python3
"""
A script that generates a .tgz archive from from the contents of a web.
"""

from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ Generates achive contents of web_static folder """

    today = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(
            today)
            )
        return "version/web_static_{}.tgz".format(today)
    except Exception as e:
        return None
