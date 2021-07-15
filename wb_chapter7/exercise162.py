##
# Compute the proportion of each alphabetic letter in a list of words
#

# Create an empty dict with letter as keys and occurences as values
letter_occurences = {}

# All the 26 letters of tha alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Open the file with the list of words
fl = open("words.txt", "r", encoding="utf-8")

# Start counting the number of words in the list
num_words = 0

# Read each line (there is one word per line)
for line in fl:
    # If the line has all uppercase letters or is an empty line, skip it
    if line.isupper() or line == "":
        continue
    # Remove EOL chars from the line
    word = line.strip()
    # For each letter in the alphabet string
    for letter in alphabet:
        # Check if the letter is in the word
        if letter in word:
            # Increment the number of occurences of 1
            letter_occurences[letter] = letter_occurences.get(letter, 0) + 1
    
    # Increment the word counter of 1
    num_words += 1

# Close the file      
fl.close()

# Find the letter with the smallest frequency
smallest_frequency = min(letter_occurences.values())
# Print the dictionary with alphabetic characters and their percentage values
for letter, number in letter_occurences.items():
    print("Letter {} occurs in {:.2f} percent of words".format(letter, number/num_words * 100))
    if number == smallest_frequency:
        smallest_letter = letter

print("\n")

# Display the letter with the lowest frequency
print("The letter with the lowest frequency is {}".format(smallest_letter))


