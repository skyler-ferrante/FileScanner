# FileScanner

Creates a sqlite database with filepaths and hash

To generate the database use:
```
./mark.py -r /etc/    #Mark all files in /etc/ recursively
./mark.py /etc/*.conf #Mark all files matching /etc/*.conf 
```

After the database is generated you can use:
```
./check.py -n       #Find all new files (Only works if mark is called with -r)
./check.py -c       #Find all changed files
./check.py -h hash  #Find files with given hash
./check.py file     #File to check if hash has changed
```

MD5 is used for hashing, and it is therefore possible to have collisions.
Using a secure hash algorithm however, would be too slow.