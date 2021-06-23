## Generate the file names in a directory tree
import os

# Get the path of the current working directory
cwd = os.getcwd()

# Print the path of each file in the root and sub-directories
output = os.walk(cwd)
for dirpath, dirnames, filenames in output:
    
    # If a sub-directory has no files, print the path till sub-directory
    if len(filenames) == 0:
        print(dirpath)
    for name in filenames:
        print(os.path.join(dirpath, name))

## Catching exceptions
try:
    with open("pippo.txt") as fl:
        lines = fl.readlines()
        print(lines)
except:
    print("Something went wrong")

## Databases
import dbm

db = dbm.open("test", "c")
db["fruit"] = "bananas"
print(db["fruit"])

## Shelve module
import shelve
with shelve.open("test2") as db:
    db["fruit"] = ["apple", "bananas", "kiwis"]
    print(db["fruit"])
   
          

