import sys
from database.database import Database
from hash import hasher

if __name__ == "__main__":
    database = Database()
    hasher.show_database_hash()

    hash_to_find = input("HASH: ")
    if len(hash_to_find) != 32:
        print("Invalid hash")
        sys.exit(1)

    files_and_hashes = database.get_all()

    for file_and_hash in files_and_hashes:
        file = file_and_hash[0]
        hash = file_and_hash[1]

        if hash == hash_to_find:
            print(file)