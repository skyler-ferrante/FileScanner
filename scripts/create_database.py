from hash import hasher
from filelist.walker import walker 
from database.database import Database

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguements")
        print("Correct usage: make_database.py directory/to/scan")
        sys.exit(1)
    path = sys.argv[1]

    database = Database()
    files = walker(path)
    print(len(files), "files")

    database.start_transaction()

    database.register_directory(path)
    for file in files:
        hash = hasher.hash_file(file)
        database.write_file(file, hash)
    
    database.end_transaction()

    hasher.show_database_hash()