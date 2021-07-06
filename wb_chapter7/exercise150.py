##
# Display only the last 10 lines of a .txt file
#

# Open a .txt file
fl = open("sample.txt", "r", encoding="utf-8")

# Store the tail lines to read in a variable
TAIL_LINES = 10

# Create an empty list to store the lines
fl_lines = []

# Read the first line
line = fl.readline()

# For each line of the file
while line != "":
    
    # Remove trailing whitespaces
    line = line.strip()
    
    # Add the line to the list
    fl_lines.append(line) 
    
    # Each time the length of the list gets greater than TAIL_LINES,
    # remove the first item
    if len(fl_lines) > TAIL_LINES:
        fl_lines.pop(0)
    
    # Move to the next line
    line = fl.readline()

# Display the last 10 lines of the file
for line in fl_lines:
    print(line)

# Close the file
fl.close()