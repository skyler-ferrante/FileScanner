#!/bin/bash
#Not great, but better then nothing

#Move main.db (if exists) to main.db.bak
if test -f "main.db";
then
    mv main.db main.db.bak
fi

#Mark /tmp/ and get amount of files changed
./mark.py /tmp/
amount_changed=$(./check.py -c | wc -l)

#Since nothing happended between marking and checking, should be 0
if test $amount_changed -ne 0; 
then
    echo "Nothing changed failed, $amount_changed change[s]"
fi

#Make a directory in /tmp/, and put a file test with contents hi in it
TMPDIR=$(mktemp -d)
echo "Hi" > $TMPDIR/test

#Since we created a file, there should be one change
amount_changed=$(./check.py -c | wc -l)
if test $amount_changed -ne 1;
then
    echo "Changed one file failed, $amount_changed change[s]"
fi

#Try to find file with hash c01a4cfa25cb895cdd0bb25181ba9c1622e93895a6de6f533a7299f70d6b0cfb
#(file with contents 'Hi')
rm main.db
./mark.py /tmp/
find_hash=$(./check.py -h c01a4cfa25cb895cdd0bb25181ba9c1622e93895a6de6f533a7299f70d6b0cfb | awk '{print $2}')
if test "$find_hash" = "$TMPDIR/test":
then
    echo "Looked for files with content Hi and got $find_hash"
fi

#Clean up
rm $TMPDIR -r

#Check how many directories registered, should be one (/tmp/)
directories=$(./info.py | tail -n 1 | awk '{print $1}')
if test $directories -ne 1;
then
    echo "Should have one directory, $directories found"
fi

# Try to update db, should have two lines of output
#   Updating...
#   Removing /tmp/tmp.Whatever/test
update_output=$(./mark.py -u | wc -l)
if test $update_output -ne 2;
then
    echo "Update had incorrect output"
fi

#Remove main.db created during this script
rm main.db
#If main.db.bak exists, move back to main.db
if test -f "main.db.bak";
then
    mv main.db.bak main.db
fi
