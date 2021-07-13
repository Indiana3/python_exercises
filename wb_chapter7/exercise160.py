##
# Compute how many words in a text follow the rule
# "I before E except after C" and display the reults
# in a .txt file
#
import re

# Store all the characters to remove in a string
chars_to_remove = "[.,;:?!=_#%0123456789/\-'\][()\"\n]"

# Open a file
fl = open("sherlock_holmes.txt", "r")

## Create an empty list to store all the words that follow the following rules:
# "IE" immediately preceded by everything but "C"
# "EI" immediately preceded by C
rule = []

## Create an empty list to store all the words that follow the following rules: 
# "IE" immediately preceded by "C"
# "EI" immediately preceded by everything but "C"
no_rule = []

# Read each line of the file
for line in fl:
    # Replace the set of characters listed in chars_to_remove variable
    # with a white space
    line = re.sub(chars_to_remove, " ", line)
    # Split the line in a list of words
    words = line.split()
    # For each word
    for i in range(len(words)):
        # Turn into lowercase letters
        words[i] = words[i].lower()
        # Check if "EI" is in the word
        position = words[i].find("ei")
        # If it's there and not at the beginning
        if position != -1 and position != 0:
            # Check if it's preceded by "C" or other letters
            if words[i][position-1:position] == "c":
                # Check if it's already in rule list
                if words[i] not in rule:
                    # Add to the rule list
                    rule.append(words[i])
            else:
                # Check if it's already in no_rule list
                if words[i] not in no_rule:
                    # Add to the no_rule list
                    no_rule.append(words[i])
        
        # Check if "IE" is in the word
        position = words[i].find("ie")
        # If it's there and not at the beginning
        if position != -1 and position != 0:
            # Check if it's preceded by "C" or other letters
            if words[i][position-1:position] == "c":
                # Check if it's already in rule list
                if words[i] not in no_rule:
                    # Add to the no_rule list
                    no_rule.append(words[i])
            else:
                # Check if it's already in rule list
                if words[i] not in rule:
                    # Add to the no_rule list
                    rule.append(words[i])     

# Close the file        
fl.close()

# Write all the words in both lists in .txt file
with open("words.txt", "w", encoding= "utf-8") as fl:
    fl.write("FOLLOW THE RULE:\n")
    for word in rule:
        fl.write(word + "\n")
    fl.write("\n" * 10)
    fl.write("DO NOT FOLLOW THE RULE:\n")
    for word in no_rule:
        fl.write(word + "\n")

