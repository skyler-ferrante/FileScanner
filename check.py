#!/bin/python3
from filescanner.filescanner import FileScanner

import sys

if __name__ == "__main__":
    filescanner = FileScanner()

    if len(sys.argv) == 1:
        print("Usage:")
        print(sys.argv[0], "-n          to find new files")
        print(sys.argv[0], "-c          to find changed files")
        print(sys.argv[0], "-h hash     to find specific hash")
        print(sys.argv[0], "file        to check specific files")
        sys.exit(1)
    argv = sys.argv[1:]

    if "-n" in argv:
        argv.remove("-n")
        filescanner.find_new_files()
    
    if "-c" in argv:
        argv.remove("-c")
        filescanner.find_changed_files()
    
    elif "-h" in argv:
        argv.remove("-h")
        for hash in argv:
            filescanner.find_by_hash(hash)
    
    else:
        for filename in argv:
            filescanner.check_file_hash(filename)