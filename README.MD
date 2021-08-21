# FileScanner

Creates a sqlite database with filepaths and hash

To generate the database use:
```
python3 -m scripts.create_database /directory/to/scan
```

After the database is generated you can use:
```
python3 -m scripts.find_by_hash #To search for a specific hash
python3 -m scripts.check_hashes #To see if any files changed
python3 -m scripts.check_new_files #To see if there is any new files
```