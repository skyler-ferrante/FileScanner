# File Scanner

Creates an sqlite database correlating filepaths to file hashes

The current state of the system can be check against this database to check for changes

This could be useful to quickly see what configuration files were changed, after something breaks

To generate the database use:
```
./mark.py /etc/         #Mark all files in /etc/ recursively (including subdirectories)
                        #Or
./mark.py /etc/*.conf   #Mark all files matching /etc/*.conf
```

After the database is generated you can use:
```
./check.py -c           #Find all changes (Only works if mark is called with directory)
./check.py -h hash      #Find files with given hash
./check.py -h <file     #Find all files with hashes in file
./check.py file         #File to check if hash has changed
./mark.py  -u           #Update database
./info.py               #Get basic information on database
```