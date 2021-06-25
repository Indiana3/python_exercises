##
# Find files with same extension .txt in tp_chapter14 directory
# and check if their content is the same or not
#
import os
import hashlib

## Find files with same extension in a directory and its subdirectories
# @param dir the root directory
# @param ext a string with file extension
# @param same_extension an empty list where store files with same extension
# @return same_extension
#
def sameExtention(dir=os.getcwd(), ext=".txt", same_extension = []):
    # Use the number of characters of extension as index
    index = len(ext)
    # For each file/directory in the root
    for name in os.listdir(dir):
        # Get its absolute path
        path = os.path.join(dir, name)
        # Check if it adresses to a file or a dir
        if os.path.isfile(path):
            #Check if the extension of the file is equal to the given extension
            if path[-index:] == ext:
                # Add it to the list
                same_extension.append(path)
        # If not a fill, call the function recursively with the new path
        else:
            sameExtention(path)
    return same_extension

# Create a list to store hashed files
hashed_files = []

# Compute a "checksum" for each file using md5 constructor function
files = sameExtention()

for file in files:
    md5_hash = hashlib.md5()
    fl = open(file, "rb")
    content = fl.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()

    # Add each hashed file to hashed files
    hashed_files.append(digest)

# Display the hashed files
for file in hashed_files:
    print(file)

