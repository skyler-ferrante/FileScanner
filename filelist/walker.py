import os
from typing import Iterable

#Will not search directories of name given in DENY_LIST
DENY_LIST = ["/mnt", "/proc", "/var", "/run"]

def walker(path : str, deny_list : Iterable = DENY_LIST):
    if not os.path.exists(path):
        raise ValueError("Path "+path+" does not exist")

    result = []

    if path[-1] == "/" and path != "/":
        path = path[0:-1]

    if path in DENY_LIST:
        raise ValueError("Tried to walk a blocked directory")

    #Get all files/dirs, not including symlinks
    for root, dirs, files in os.walk(path):
        for deny in deny_list:
            dirs[:] = [dir for dir in dirs if not (root+dir).startswith(deny)]

        root = root+"/"

        #Walk includes broken symlinks and special files, so we check isFile
        result.extend([root+file for file in files if os.path.isfile(root+file)])
    
    return result