#!/bin/python3
from main.filescanner import FileScanner
import sys

if __name__ == "__main__":
    filescanner = FileScanner()    

    if len(sys.argv) == 1:
        print("Usage:")
        print(sys.argv[0], "file            Mark file")
        print(sys.argv[0], "directory -r    Mark directory recursive")
        print(sys.argv[0], "-u              Update")
        sys.exit(1)
    filenames = sys.argv[1:]

    if "-u" in filenames:
        print("Updating...")
        filescanner.update_file_hashes()

    elif "-r" in filenames:
        filenames.remove("-r")
        for file in filenames:
            filescanner.mark_directory_recursive(file)
    else:
        print(len(filenames), "files")
        filescanner.mark_files(filenames)

    filescanner.show_database_hash()