#!/bin/python3
from database.database import Database

if __name__ == "__main__":
    # filescanner = FileScanner()
    database = Database()

    files = database.get_all_files().fetchall()

    directories = database.get_directories().fetchall()
    for directory in directories:
        print(directory[0])
    
    print(len(files), "files")
    print(len(directories), "directories")
