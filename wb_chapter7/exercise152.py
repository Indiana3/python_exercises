##
# Number the lines of a file and store the numbered lines
# into a new file
#
import sys

# Open a file
fl = open(sys.argv[1], "r", encoding="utf-8")

# Create a new file to store the numbered lines
fl2 = open(sys.argv[2], "a", encoding="utf-8")

# Start counting lines from the first one
num = 1

# Read the first line
line = fl.readline()

# Until line is not empty
while line != "":

    # Write the line in the new file preceded by its number, a colon and a space
    fl2.write(str(num) + ", " + line)
    
    # Move to the next line
    line = fl.readline()
    
    # Add 1 line to the counter
    num += 1

# Close files
fl.close()
fl2.close()

