##
# Check if there are repeated words in a text file
#
import sys
import re

# Check if the user entered the file to examine as a command line argument
if len(sys.argv) != 2:
    print("An argument is missing.")
    print("Quitting...")
    quit()

try:
    # Open the file entered by the user
    fl = open(sys.argv[1], "r", encoding="utf-8")
    # Read the first line
    line = fl.readline().strip()
    # Line counter starts at 1
    num = 1
    # Create a tuple with 2 empty strings
    # It will store the previous and the following word to check
    prev_next = ("", "")
    # Until line is not an empty line
    while line != "":
        # Remove punctuation marks
        line = re.sub("[,;.:!?]", "", line)
        # Split the line in a list of words
        words = line.split()
        # For each word
        for i in range(len(words)):
            # Turn it into lowercase chars
            words[i] = words[i].lower()
            # The new tuple will store the second element (the following word, now the previous one)
            # and the following word in the text
            prev_next = prev_next[1:] + (words[i],)
            # If the 2 words are equal, print a message with the repeated word and the number of line  
            if prev_next[0] == prev_next[1]:
                print("Repeated '{}' at line {}".format(prev_next[1], num))
        # Read the following line
        line = fl.readline().strip()
        # Increment the line counter of one
        num += 1
    # Close the file
    fl.close()
except:
    # Print an error message
    print("The file you entered doesn't exist or you spelled it wrong.")