#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script generates .tgz archive of all in web_static/ using func 'do_pack'
Usage: fab -f 1-pack_web_static.py do_pack
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder 'versions' (create folder if none)
Create archive "web_static_<year><month><day><hour><minute><second>.tgz"
The function do_pack must return the archive path, else return None
"""

from fabric.api import local
from time import strftime


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



=======
    Script generates a .tgz archive from web_static folder
"""


def do_pack():
    """
    function creates a .tgz
    """
    from fabric.operations import local
    from datetime import datetime

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None

if __name__ == "__main__":
    do_pack()
>>>>>>> 1aced92aa093f0aa05e999d8e476b453e47af141
