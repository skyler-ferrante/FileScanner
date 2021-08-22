#!/bin/python3
# from database import *

import database.database

import hashlib
import sys

def hash_file(filename, hasher = hashlib.sha256) -> str:
    hasher = hasher()
    
    #Open file in binary mode
    with open(filename, "rb") as file:
        #Read whole file, faster in testing, but uses more ram
        data = file.read()
        hasher.update(data)

        #Read file in 65536 byte chunks
        # while True:
        #     data = file.read(65536)
        #     if not data:
        #         break
        #     hasher.update(data)
    
    return hasher.hexdigest()

def show_database_hash():
    """Used to make sure the database is not modified"""
    
    database_filename = database.database.DATABASE_FILE_NAME
    database_hash = hash_file(database_filename)
    
    #prints database hash to stderr, so it's not piped
    print("DB HASH: "+database_hash, file=sys.stderr)