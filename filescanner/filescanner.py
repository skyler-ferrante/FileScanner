from typing import Iterable
import os.path
from hash import hasher
from filelist.walker import walker 
from database.database import Database

import sys

class FileScanner():
    __slots__ = ["database"]

    def __init__(self) -> None:
        self.database = Database()

    def mark_file(self, filename : str):
        hash = hasher.hash_file(filename)
        self.database.write_file(filename, hash)

    def mark_files(self, filenames : Iterable):
        self.database.start_transaction()
        
        for filename in filenames:
            self.mark_file(filename)            

        self.database.end_transaction()

    def mark_directory_recursive(self, path):
        filenames = walker(path)
        self.mark_files(filenames)

        self.database.start_transaction()
        self.database.register_directory(path)
        self.database.end_transaction()

    def mark_directories_recursive(self, paths):
        for path in paths:
            self.mark_directory_recursive(path)

    def update_file_hashes(self):
        paths = self.database.get_directories()
        paths = [path[0] for path in paths]

        registered_files = self.database.get_all_files()
        registered_files = [file[0] for file in registered_files]

        self.database.start_transaction()
        #Find and update all new files
        for path in paths:
            all_files = walker(path)

            for file in all_files:
                if file not in registered_files:
                    print("New file", file)
                    self.mark_file(file)
        #Update all old files
        for filepath in registered_files:
            if not os.path.isfile(filepath):
                print("Removing",filepath)
                self.database.remove_file(filepath)
                registered_files.remove(filepath)
        self.database.end_transaction()

        self.mark_files(registered_files)

    def check_file_hash(self, filename):
        new_hash = hasher.hash_file(filename)
        old_hash = self.database.get_by_filepath(filename).fetchall()
        if len(old_hash) == 0:
            print(filename, "not in database")
            return
        old_hash, = old_hash[0]

        if new_hash != old_hash:
            print(filename, "new:", new_hash, "old:", old_hash)

    def find_new_files(self):
        paths = self.database.get_directories()
        paths = [path[0] for path in paths]

        registered_files = self.database.get_all_files()
        registered_files = [file[0] for file in registered_files]

        for path in paths:
            all_files = walker(path)

            for file in all_files:
                if file not in registered_files:
                    hash = hasher.hash_file(file)
                    print(file, "created", hash)

    def find_changed_files(self):
        files_and_hashes = self.database.get_all()

        for file_and_hash in files_and_hashes:
            file = file_and_hash[0]
            orginal_hash = file_and_hash[1]
            try:
                new_hash = hasher.hash_file(file)
            except FileNotFoundError:
                print(file, "removed")
                break

            if orginal_hash != new_hash:
                print(file,"changed",new_hash)
    
    def find_by_hash(self, hash):
        for file in self.database.get_by_hash(hash):
            print(hash, file[0])

    def show_database_hash(self):
        hasher.show_database_hash()