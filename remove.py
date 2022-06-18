
#!/usr/bin/python
import os
import sys
import shutil

# Get directory name
mydir= input("Enter directory name: ")

try:
    shutil.rmtree(mydir)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))