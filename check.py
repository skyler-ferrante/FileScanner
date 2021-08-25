#!/bin/python3
from filescanner.filescanner import FileScanner

import sys

if __name__ == "__main__":
    filescanner = FileScanner()

    if len(sys.argv) == 1:
        print("Usage:")
        print(sys.argv[0], "-c          to find changes")
        print(sys.argv[0], "-h hash     to find specific hash")
        print(sys.argv[0], "file        to check specific files")
        sys.exit(1)
    argv = sys.argv[1:]

    if "-c" in argv:
        argv.remove("-c")
        filescanner.find_new_files()
        filescanner.find_changed_files()
    elif "-h" in argv:
        argv.remove("-h")
        for hash in argv:
            filescanner.find_by_hash(hash)
    else:
        for filename in argv:
            filescanner.check_file_hash(filename)