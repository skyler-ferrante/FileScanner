#!/bin/python3
from filescanner.filescanner import FileScanner
import sys
import os

if __name__ == "__main__":
    filescanner = FileScanner()

    # Remove running file from argv
    args = sys.argv[1:]

    # If no arguments given, print help message and exit
    if len(args) == 0:
        print("Usage:")
        print(sys.argv[0], "file            Mark files or directories")
        print(sys.argv[0], "-u              Update")
        sys.exit(0)

    # If -u, Update database
    if "-u" in args:
        args.remove("-u")
        print("Updating...")
        filescanner.update_file_hashes()

    files = []
    directories = []
    unknowns = []

    # For every argument given, check if file or directory
    for arg in args:
        if os.path.isfile(arg):
            files.append(arg)
        elif os.path.isdir(arg):
            directories.append(arg)
        else:
            unknowns.append(arg)

    # Mark every file and directory that is given as arguments
    filescanner.mark_files(files)
    filescanner.mark_directories_recursive(directories)

    # For all arguments given that are not files or directories, print error message
    for unknown in unknowns:
        print(unknown, "is not a known flag, file, or directory")