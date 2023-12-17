#!/usr/bin/python3

import os.path
from datetime import datetime
from fabric.api import *

env.hosts = ['18.207.142.8', '52.86.87.208']
env.user = 'ubuntu'


def do_pack():
    """
    Creates and distributes an archive to the web server.
    """
    dat = datetime.now()
    dfile = 'versions/web_static_{}{}{}{}{}{}'.format(
            dat.year, dat.month, dat.day, dat.hour, dat.minute, dat.second
            )

    if os.path.isdir('versions') is False:
        if local('mkdir -p versions').failed is True:
            return None
    if local('tar -cvzf {} web_static'.format(dfile)).failed is True:
        return None
    return dfile


def do_deploy(archive_path):
    """
    Distributes archives to web servers.
        Argument: archive_path -> String path to the archive file/s
    """
    if os.path.isfile(archive_path) is False:
        return False
    a_file = archive_path.split('/')[-1]
    f_name = a_file.split('.')[0]

    if put(archive_path, '/tmp/{}'.format(a_file)).failed is True:
        return False

    if run(
            'rm -rf /data/web_static/releases/{}/'.format(f_name)
            ).failed is True:
        return False

    if run(
            'mkdir -p /data/web_static/releases/{}/'.format(f_name)
            ).failed is True:
        return False

    if run(
            'tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
                a_file, f_name
                )
            ).failed is True:
        return False

    if run('rm /tmp/{}'.format(a_file)).failed is True:
        return False

    if run(
            'mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(f_name, f_name)
            ).failed is True:
        return False

    if run(
            'rm -rf /data/web_static/releases/{}/web_static'.format(f_name)
            ).failed is True:
        return False

    if run('rm -rf /data/web_static/current').failed is True:
        return False

    if run(
            'ln -s /data/web_static/releases/{} /data/web_static/current'.
            format(f_name)
            ).failed is True:
        return False

    return True


def deploy():
    """ Creates and distributes an archive to a web server"""
    recall = do_pack()
    if recall is None:
        return False
    return do_deploy(recall)
