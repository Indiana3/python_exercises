##
# Generate 2 word random password
#
import random

# Opena a file with a list of English words
fl = open("build_passwords.txt", "r", encoding="utf-8")

# Create an empty list to store the English words
words = []

# For each line of the file
for line in fl:
    # Remove the EOL chars
    line = line.strip()
    # Add the line (word) to the list
    words.append(line)

# Close the file
fl.close()

while True:
    # Select randomly the first word from the list
    word1 = random.choice(words)
    # Remove the selected word from the list
    words.remove(word1)
    # Select randomly the second word from the list
    word2 = random.choice(words)
    # Check if both word lengths are equal or greater than 3
    if len(word1) >= 3 and len(word2) >= 3:
        # Check if the sum of lengths is between 8 and 10 characters
        if len(word1+word2) >= 8 and len(word1+word2) <= 10:
            # Capitalize both words
            word1 = word1.capitalize()
            word2 = word2.capitalize()
            break
    # Add again the first word to the list and start another loop
    words.append(word1)

# Display the two word random password    
print(word1+word2)

