#!/usr/bin/python3
""" A script based on the file 1-pack_web_static.py
"""

from fabric.api import *
from datetime import datetime
from os import path

# Servers to log in to
env.hosts = ['18.207.142.8', '52.86.87.208']
env.user = 'ubuntu'


# Function to deploy
def do_deploy(archive_path):
    """ Deploys a web file to server. """
    try:
        if not (path.exist(archive_path)):
            return False

        # Achive upload
        put(archive_path, '/tmp')

        # Target directory
        archive_time = archive_path[-18:-4]
        run(
                'sudo mkdir -p /data/web_static/releases/web_static_{}'.format(
                    archive_time)
                )

        # Uncompress archive and delete .tgz files.
        run(
                'sudo tar -xzf /tmp/web_static_{}.tgz -c\
                /data/web_static_releases/web_static_{}/'.format(
                    archive_time, archive_time)
                )

        # Removes archive files.
        run('sudo rm /tmp/web_static_{}.tgz'.format(archive_time))

        # Move the contents into the host web_static
        run(
                'sudo mv /data/web_static/releases/web_static_{}/web_static/*\
                /data/web_static/releases/web_static_{}/'.format(
                    archive_time, archive_time)
                )

        # Remove extraneous web_static directory
        run(
                'sudo rm -rf /data/web_static/releases/\
                web_static_{}/web_static'.format(archive_time)
                )

        # Delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Re-establish symbolic link
        run(
                'sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current'.format(archive_time)
                )

    except Exception as e:
        return False

    # Otherwise True is return
    return True
