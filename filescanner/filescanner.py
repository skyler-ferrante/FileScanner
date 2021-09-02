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
        """Hash file, and add filename and hash to database"""
        hash = hasher.hash_file(filename)
        self.database.write_file(filename, hash)

    def mark_files(self, filenames : Iterable):
        """
        Call mark_file on every filename in filenames.
        Uses sql transactions.
        """
        self.database.start_transaction()
        
        for filename in filenames:
            self.mark_file(filename)            

        self.database.end_transaction()

    def mark_directory_recursive(self, path):
        """Add directory, subdirectories, and files to database"""
        filenames = walker(path)
        self.mark_files(filenames)

        self.database.start_transaction()
        self.database.register_directory(path)
        self.database.end_transaction()

    def mark_directories_recursive(self, paths):
        """Call mark_directory_recursive on all paths"""
        for path in paths:
            self.mark_directory_recursive(path)

    def update_file_hashes(self):
        """
        Update database with new/changed files in registered directories recursively.
        Uses sql transactions.
        """
        #Get all registered directories
        paths = self.database.get_directories()
        paths = [path[0] for path in paths]

        #Get all registered files
        registered_files = self.database.get_all_files()
        registered_files = [file[0] for file in registered_files]

        self.database.start_transaction()
        
        #Find and mark all new files
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
        """Print file changes to stdout"""
        old_hash = self.database.get_by_filepath(filename).fetchall()
        
        #File not in database
        if len(old_hash) == 0:
            print(filename, "not in database")
            return
        old_hash, = old_hash[0]
        
        try:
            #File changed
            new_hash = hasher.hash_file(filename)
            if old_hash != new_hash:
                print(filename,"changed",new_hash)
        
        except FileNotFoundError:
            #File removed
            print(filename,"removed")

    def find_new_files(self):
        """Print new files to stdout"""
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
        """Run check_file_hash on all files"""
        files = self.database.get_all_files()
        files = [file[0] for file in files]
        for file in files:
            self.check_file_hash(file)

    def find_by_hash(self, hash):
        """
        Find file by hash in database.
        Does not walk files/use new file contents.
        """
        for file in self.database.get_by_hash(hash):
            print(hash, file[0])