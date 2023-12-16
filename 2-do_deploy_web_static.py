#!/usr/bin/python3
"""
script based on the file 1-pack_web_static.py
"""
from fabric.api import *
from datetime import datetime
import os.path

# Servers to log in to
env.hosts = ['18.207.142.8', '52.86.87.208']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Deploys web files to a server.
    """

    if not os.path.exists(archive_path):
        return False

    file_name = archive_path.split('/')
    new_name = file_name[1]
    n_var = new_name.split('.')
    path_tar = "/data/web_static/releases/{}/".format(n_var[0])
    symbolic_link = "/data/web_static/current"

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_tar))
        run("tar -xzf /tmp/{} -C {}".format(new_name, path_tar))
        run("rm /tmp/{}".format(new_name))
        run("mv {}web_static/* {}".format(path_tar, path_tar))
        run("rm -rf {}".format(symbolic_link))
        run("ln -s {} {}".format(path_tar, symbolic_link))
        return True
    except Exception as e:
        return False
