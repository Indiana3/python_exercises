##
# Check if a .txt file contains words with spelling mistakes
#
import sys
import re

# Check if the user entered the file to check as a command line argument
if len(sys.argv) != 2:
    print("Command line argument missing")
    quit()

# Create an empty dictionary to store the words as keys
# from the list of known words
known_words = {}

# Open the file containing the list of known words
fl = open("known_words.txt", "r", encoding="utf-8")
# Read the first line and remove EOL chars
line = fl.readline().strip()
# While line is not an empty line
while line != "":
    # Add the line to the dictionary of known words
    known_words[line] = ""
    # Read the next line
    line = fl.readline().strip()
# Close the file
fl.close()

# Try to open the file to check for spelling mistakes
# entered by the user
try:
    fl = open(sys.argv[1], "r", encoding="utf-8")
    # Read the first line and remove EOL chars
    line = fl.readline().strip()
    # While line is not an empty line
    while line != "":
        # Split line in a list of words
        words = line.split()
        # For each word of the line
        for word in words:
            # Remove punctuation marks
            word = re.sub("[.,;:!?]", "", word)
            # Turn to lowercase chars
            word = word.lower()
            # Check if the word is in the keys list of known words dictionary
            # If not, display a spelling mistake
            if word not in known_words.keys():
                print("The word '{}' has a spelling mistake".format(word))
        # Read the next line
        line = fl.readline().strip()
    # Close the file
    fl.close()
# Print an error message
except:
    print("Probably you didn't spelled the file's name correctly")