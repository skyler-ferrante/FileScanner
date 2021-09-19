#!/bin/python3

import hashlib
import os
from stat import ST_MODE

def hash(filename, hasher = hashlib.sha256) -> str:
    hasher = hasher()
    
    #Open file in binary mode
    with open(filename, "rb") as file:
        # Read file in 65536 byte chunks
        while True:
            data = file.read(65536)
            if not data:
                break
            hasher.update(data)
    
    return hasher.hexdigest()

def permissions(filename):
    stat = os.stat(filename)
    #Ex 755
    permissions = int(oct(stat[ST_MODE])[-3:])
    return permissions