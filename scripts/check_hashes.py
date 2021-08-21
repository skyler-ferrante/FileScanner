from database.database import Database
from hash import hasher

if __name__ == "__main__":
    database = Database()
    hasher.show_database_hash()

    files_and_hashes = database.get_all()

    for file_and_hash in files_and_hashes:
        file = file_and_hash[0]
        orginal_hash = file_and_hash[1]
        new_hash = hasher.hash_file(file)

        if orginal_hash != new_hash:
            print(file+" "+new_hash)