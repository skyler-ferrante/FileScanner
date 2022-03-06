# File Scanner

Creates an sqlite database correlating filepaths to file hashes and permissions

The current state of the system can be checked against this database to find changes

To generate the database use:
```
./mark.py /etc/              #Mark all files in /etc/ recursively (including subdirectories)
                             #Or
./mark.py /etc/*.conf        #Mark all files matching /etc/*.conf
```

After the database is generated you can use:
```
./check.py -c                #Find all changes (Only works if mark is called with directory)
./check.py -h hash           #Find files with given hash
./check.py -p permission     #Find files with given permission
./check.py -h <file          #Find all files with hashes in file
./check.py file              #File to check if hash has changed
./mark.py  -u                #Update database
./info.py                    #Get basic information on database
```

Note: Default ignores the directories /mnt, /proc, /var, and /run

This can be changed in filelist/walker.py

Create binaries with pyinstaller:
```
make
``` 
