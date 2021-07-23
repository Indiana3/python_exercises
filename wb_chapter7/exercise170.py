##
# Check if there are missing comments functions
#
import sys

# For all the file names entered by the user
for i in range(1, len(sys.argv)):
    try:
        # Open the file
        fl = open(sys.argv[i], "r", encoding="utf-8")
        # Create a tuple to store pairs of previous-following lines
        prev_next = ("", "")
        # Start to count the first line
        num = 1
        # Read the first line
        line = fl.readline()
        # While the line is not empty
        while line != "":
            # Remove EOL char
            line = line.strip()
            # In the new pair of lines, the one that was in second position passes to first
            # and the new line takes its place
            prev_next = prev_next[1:] + (line,)
            # Assign the 2 elements to different variables
            prev, next = prev_next
            # If the first character of previous line is different from "#" and
            # the first four characters of following line are equal to "def ",
            # print a message of missing comments function along with the number of line and the file name
            if prev[:1] != "#" and next[:4] == "def ":
                print("Function header at line", num, "with no comments in file", sys.argv[i])
            # Read the following line
            line = fl.readline()
            # Count the following line
            num += 1
        # Close the file
        fl.close()
    except:
        # Print an error message
        print("Probably the file doesn't exist or you spelled it wrong")