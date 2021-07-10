##
# Remove comments from a .txt file
#
import sys

# Check if 2 file names are entered by the user
if len(sys.argv) != 3:
    print("One or more files missing...")
    quit()

try:
    # Open the file where there are comments to remove
    fl = open(sys.argv[1], "r")

except FileNotFoundError:
    # Display an error message if the file does not exist
    print("This file does not exist")

# Open the new file where coping the previous file without comments
new_file = open(sys.argv[2], "w")

# For each line of the file
for line in fl:
    # Check if a "#" character is in the line 
    pos = line.find("#")
    if pos > -1:
        # If so, remove all the characters of the line
        line = line[0:pos]
        line = line + "\n"
    # Copy the line in the new file
    new_file.write(line)

# Close the file
fl.close()

# Close the new file
new_file.close()