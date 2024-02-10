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

Example (finding new crontabs)
```
$ sudo ./mark.py /var/ # Keep track of var
$ sudo ./check.py -c # Look for changes (none)
$ (crontab -l; echo "* * * * * /home/user/some_script3.sh") | crontab - # Add crontab entry
$ sudo ./check.py -c # Look for changes (should find crontab modification)
/var/spool/cron/crontabs/sky modified 144422a6890f794dc69900d94ec92f0d603e85dbd382754399938d967e96bff7
```

Create binaries with pyinstaller:
```
make
``` 

Note: Default ignores the directories /mnt, /proc, /var, and /run

This can be changed in filelist/walker.py
