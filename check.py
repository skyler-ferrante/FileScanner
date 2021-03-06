#!/bin/python3
import sys
import os
from filescanner.filescanner import FileScanner

if __name__ == "__main__":
    filescanner = FileScanner()

    # Remove running file from argv
    argv = sys.argv[1:]

    # If no arguments given, print help message and exit
    if len(argv) == 0:
        print(sys.argv[0], "-c              find changes")
        print(sys.argv[0], "-h hash         find specific hash (stdin if no hash given)")
        print(sys.argv[0], "-p permission   find specific permission (stdin if no hash given)")
        print(sys.argv[0], "file            check specific files")
        sys.exit(1)

    # Find changes (new/changed files)
    if "-c" in argv:
        argv.remove("-c")
        filescanner.find_new_files()
        filescanner.find_changed_files()
        if len(argv) != 0:
            print("-c causes all other arguments to be ignored")
    
    # Find specific hash/hashes,
    #   if other arguments given, use those as hashes
    #   if no other arguments given, use stdin until EOF
    # Checks database, so does not know if file has changed to given hash
    elif "-h" in argv:
        argv.remove("-h")
        if len(argv) == 0:
            argv = sys.stdin
        for hash in argv:
            hash = hash.strip()
            filescanner.find_by_hash(hash)

    # Find specific permission
    #   if other arguments given use those as permissions
    #   if no other arguments given, use stdin until EOF
    # Checks database, so does not know if file permissions have changed
    elif "-p" in argv:
        argv.remove("-p")
        if len(argv) == 0:
            argv = sys.stdin
        for permissions in argv:
            permissions = int(permissions.strip())
            filescanner.find_by_permissions(permissions)
    
    # Only check specific files/dirs for changes
    else:
        files = []
        directories = []
        unknowns = []

        # For every argument given, check if file or directory
        for arg in argv:
            if os.path.isfile(arg):
                files.append(arg)
            elif os.path.isdir(arg):
                directories.append(arg)
            else:
                unknowns.append(arg)
        
        filescanner.check_files(files)
        filescanner.check_dirs(directories)

        for unknown in unknowns:
            print(unknown, "is not a known flag, file, or directory")