#!/bin/python3
from main.filescanner import FileScanner
import sys
import os

if __name__ == "__main__":
    filescanner = FileScanner()    

    if len(sys.argv) == 1:
        print("Usage:")
        print(sys.argv[0], "file            Mark files or directories")
        print(sys.argv[0], "-u              Update")
        sys.exit(0)
    args = sys.argv[1:]

    if "-u" in args:
        args.remove("-u")
        print("Updating...")
        filescanner.update_file_hashes()

    files = []
    directories = []
    unknowns = []

    for arg in args:
        if os.path.isfile(arg):
            files.append(arg)
        elif os.path.isdir(arg):
            directories.append(arg)
        else:
            unknowns.append(arg)

    filescanner.mark_files(files)
    filescanner.mark_directories_recursive(directories)

    for unknown in unknowns:
        print(unknown, "is neither a known flag, file, or directory")

    filescanner.show_database_hash()