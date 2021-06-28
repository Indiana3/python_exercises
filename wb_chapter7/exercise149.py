##
# Print the first 10 lines of a .txt file
#
from sys import argv

try:
    # Open the file
    fl = open(argv[1], "r", encoding="utf-8")

    # Number of lines to read
    NUM_LINES_TO_READ = 10

    # Start from the first line
    num_line = 1

    # For each of the first ten lines
    while num_line <= NUM_LINES_TO_READ:
        # Read the line
        line = fl.readline()
        
        # Remove end line chars
        line = line.strip()
        
        # Print the line
        print(line)
        
        # Move to the next line
        num_line += 1
    
    # Close the file
    fl.close()

# Catch more probable errors
except IndexError:
    print("You omitted a command line argument")

except FileNotFoundError:
    print("The file you entered doesn't exist")
