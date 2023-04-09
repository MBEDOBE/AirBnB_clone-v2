#!/usr/bin/python3
"""
Fabric script methods:
    do_pack: packs web_static/ files into .tgz archive
    do_deploy: deploys archive to webservers
    deploy: do_packs && do_deploys
Usage:
    fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
from fabric.api import local, env, put, run
from time import strftime
import os.path
env.hosts = ['18.209.178.197', '18.204.20.146']
def do_pack():
    """generate .tgz archive of web_static/ folder"""
    datetime = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(datetime)
        local("tar -cvzf {} web_static/".format(file_name))
        return file_name
    except:
        return None
def do_deploy(archive_path):
    """
    Deploy archive to web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path_no_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except:
        return False
def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success



