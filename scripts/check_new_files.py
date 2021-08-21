from hash import hasher
from filelist.walker import walker
from database.database import Database

if __name__ == "__main__":
    database = Database()

    paths = database.get_directories()
    paths = [path[0] for path in paths]

    registered_files = database.get_all_files()
    registered_files = [file[0] for file in registered_files]

    for path in paths:
        all_files = walker(path)

        for file in all_files:
            if file not in registered_files:
                hash = hasher.hash_file(file)
                print(file, hash)