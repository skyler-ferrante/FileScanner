import sqlite3

DATABASE_FILE_NAME = "database/main.db"

#Reuses same database connection
class Database:
    __slots__ = ["database", "cursor"]

    def __init__(self) -> None:
        self.database = sqlite3.connect(DATABASE_FILE_NAME)
        self.cursor = self.database.cursor()
    
        #Create table with filename (4096 is max linux filepath) and hash (md5 is 32)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS file( 
                filepath VARCHAR(4096) UNIQUE, 
                hash CHARACTER(32)
        )""")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS directory(
                directorypath VARCHAR(4096) UNIQUE
        )""")
        
        self.database.commit()
    
    def start_transaction(self):
        self.cursor.execute("BEGIN")
    
    def end_transaction(self):
        self.cursor.execute("END")
        # self.cursor.execute("COMMIT")
        self.database.commit()

    # Note: this will autoreplace values already entered
    def write_file(self, file_name : str, hash : str):
        self.cursor.execute("INSERT OR REPLACE INTO file VALUES (?, ?)", (file_name, hash))

    # Note: this will autoreplace values already entered
    def register_directory(self, directory):
        self.cursor.execute("INSERT OR REPLACE INTO directory VALUES (?)", (directory,))

    # NOTE: THESE ARE USING THE SAME DATABASE CONNECTION, put data into something before calling another database method
    # DATA WILL BE CLEARED IF ANOTHER DATABASE METHOD IS CALLED

    def get_all(self) -> list:
        return self.cursor.execute("SELECT * FROM file")

    def get_all_files(self) -> list:
        return self.cursor.execute("SELECT filepath FROM file")

    def get_by_hash(self, hash : str) -> list:
        return self.cursor.execute("SELECT filepath FROM file WHERE hash=(?)", (hash,))

    def get_by_filepath(self, filepath : str):
        return self.cursor.execute("SELECT hash FROM file WHERE filepath=(?)", (filepath,))

    def get_directories(self) -> list:
        return self.cursor.execute("SELECT directorypath FROM directory")