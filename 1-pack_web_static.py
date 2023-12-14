#!/usr/bin/python3
"""
A script that generates a .tgz archive from from the contents of a web.
"""

from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    today = datetime.datetime.now()
    time_format = today.strftime("%Y%m%d%H%M%S")
    web_version = f'version/web_static{time_format}.tgz'

    try:
        local("mkdir -p versions")
        local(f'tar -cvzf {web_version} web_static')
        return web_version
    except Exception as e:
        return None
