import os
import hashlib

def sameExtention(dir=os.getcwd(), ext=".txt", same_extension = []):
    index = len(ext)
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            if path[-index:] == ext:
                same_extension.append(path)
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

