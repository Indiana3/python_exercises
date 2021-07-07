##
# Compute and display the frequencies of words in a .txt file
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

    # Dict to store words/freqs
    words_freq = {}

    # Chars to remove from lines
    to_remove = "[.,;!?':\"\n0123456789]"

    # Start with the first line
    line = fl.readline()

    # For each line
    while line != "":
        # Remove the set of chars
        line = re.sub(to_remove, "", line)
        # Split the line in a list of words
        words = line.split()
        # Traverse the list and count the occurences of
        # each word
        for word in words:
            word = word.lower()
            if word not in words_freq:
                words_freq[word] = 1
            else:
                words_freq[word] += 1
        
        # Move to the next line
        line = fl.readline()

    # Display letters with their frequencies
    print("Word\t\tFrequence")
    for word, freq in words_freq.items():
        print(word.ljust(10), "\t", freq)
    
    # Close the file
    fl.close()

# Display an error message if the file can't be opened
except FileNotFoundError:
    print("The file you entered could have been typed uncorrectly or could not exist")