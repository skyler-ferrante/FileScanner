#!/bin/python3

import urllib.request
from time import sleep

#Taken from, https://virusshare.com/hashes
#About 1.1G

#Links take the form of:
# https://virusshare.com/hashfiles/VirusShare_00000.md5
# https://virusshare.com/hashfiles/VirusShare_00001.md5
# etc.

URL = "https://virusshare.com/hashfiles/VirusShare_"
ENDING = ".md5"

if __name__ == "__main__":
    for i in range(390):
        i = str(i)
        padding = '0'*(5-len(i))
        hashurl = URL+padding+i+ENDING

        print(hashurl)

        with urllib.request.urlopen(hashurl) as f:
            content = f.read()
            
            disk_file = open("data/"+padding+i+".txt", "wb")
            disk_file.write(content)
            disk_file.close()

            sleep(2) #Help make virusshare not hate me