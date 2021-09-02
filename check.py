#!/bin/python3
from filescanner.filescanner import FileScanner

import sys

if __name__ == "__main__":
    filescanner = FileScanner()

    # Remove running file from argv
    argv = sys.argv[1:]

    # If no arguments given, print help message and exit
    if len(argv) == 0:
        print("Usage:")
        print(sys.argv[0], "-c          to find changes")
        print(sys.argv[0], "-h hash     to find specific hash (stdin if no hash given)")
        print(sys.argv[0], "file        to check specific files")
        sys.exit(1)

    # Find changes (new/changed files)
    if "-c" in argv:
        argv.remove("-c")
        filescanner.find_new_files()
        filescanner.find_changed_files()
        if len(argv) != 0:
            print("-c causes all other arguments to be ignored")
    
    # Find specific hash/hashes,
    #   if other arguments given, use thoses as hashes
    #   if no other arguments given, use stdin until EOF
    # Checks database, so does not know if file has changed to given hash
    elif "-h" in argv:
        argv.remove("-h")
        if len(argv) == 0:
            argv = sys.stdin
        for hash in argv:
            hash = hash.strip()
            filescanner.find_by_hash(hash)
    
    # Only check specific file for changes
    else:
        for filename in argv:
            filescanner.check_file_hash(filename)