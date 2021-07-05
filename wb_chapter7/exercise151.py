##
# Concatenate one or more files
#
import sys

# Check if at least 1 command line argument except the running file was provided
if len(sys.argv) == 1:
    print("You didn't enter any file to concatenate")
    quit()

# For each .txt file to display
for i in range(1, len(sys.argv)):
    f_name = sys.argv[i]
    try:

        # Open the current file for reading
        fl = open(f_name, "r", encoding="utf-8")
        
        # Display each line of the file
        for line in fl:
            print(line, end="")
        
        # Close the file
        fl.close()
    
    # Print a message of error if the file can be opened
    except:
        print("The current file can't be opened")





    
    
    