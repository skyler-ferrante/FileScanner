#!/bin/python3
from main.filescanner import FileScanner
import sys

if __name__ == "__main__":
    filescanner = FileScanner()    

    if len(sys.argv) == 1:
        print("Usage:", sys.argv[0], "files")
        print("Or: ", sys.argv[0], "directory", "-r")
        sys.exit(1)
    filenames = sys.argv[1:]

    if "-r" in filenames:
        filenames.remove("-r")
        for file in filenames:
            filescanner.mark_directory_recursive(file)
    else:
        print(len(filenames), "files")
        filescanner.mark_files(filenames)

    filescanner.show_database_hash()