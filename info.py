#!/bin/python3
from database.database import Database

if __name__ == "__main__":
    database = Database()

    # Gets all files and directories from database
    files = database.get_all_files().fetchall()
    directories = database.get_directories().fetchall()

    # Prints all registered directories
    for directory in directories:
        print(directory[0])

    # Prints the amount of files and directories
    print(len(files), "files")
    print(len(directories), "directories")
