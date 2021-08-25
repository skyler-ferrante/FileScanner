# FileScanner

Creates a sqlite database with filepaths and hash

Uses file hashes to find file changes

This could be useful to quickly see what configuration files were changed, after something breaks

Generating the database and looking for changes only takes a second or two on my machine, using the directory /etc/

To generate the database use:
```
./mark.py /etc/         #Mark all files in /etc/ recursively (including subdirectories)
./mark.py /etc/*.conf   #Mark all files matching /etc/*.conf
```

After the database is generated you can use:
```
./check.py -c           #Find all changes (Only works if mark is called with directory)
./check.py -h hash      #Find files with given hash
./check.py file         #File to check if hash has changed
./mark.py  -u           #Update database
./info.py               #Get basic information on database
```