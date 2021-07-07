##
# Compute and display the frequencies of all the letters
# in a .txt file
#
import sys
import re

# Check if the user entered the file name by command line
if len(sys.argv) != 2:
    print("File name missing...")
    quit()

try:
    # Open the file
    fl = open(sys.argv[1], "r", encoding="utf-8")

    # Dict to store chars/freqs
    letter_freq = {}

    # Chars to remove from lines
    to_remove = "[.,;!?':\"\n ]"

    # Start with the first line
    line = fl.readline()

    # For each line
    while line != "":
        # Remove the set of chars
        line = re.sub(to_remove, "", line)
        # Traverse the line and store each different letter
        # and its frequency in the dict
        for ch in line:
            ch = ch.lower()
            if ch not in letter_freq:
                letter_freq[ch] = 1
            else:
                letter_freq[ch] += 1
        
        # Move to the next line
        line = fl.readline()

    # Display letters with their frequencies
    print("Letter\tFrequence")
    for letter, freq in letter_freq.items():
        print(letter, "\t", freq)
    
    # Close the file
    fl.close()

# Display an error message if the file can't be opened
except FileNotFoundError:
    print("The file you entered could have been typed uncorrectly or could not exist")