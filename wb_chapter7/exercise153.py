##
# Identify the longest word in a .txt file
#

# Open a .txt file
fl = open("sample.txt", "r", encoding="utf-8")

# Create an empty dictionary to store the length of the words as keys
# and the corresponding words as values
len_words = {}

# For each line of the file
for line in fl:

    # Remove EOL char
    line = line.strip()
    
    # Store all the words in a list
    line_words = line.split()
    
    # For each word
    for word in line_words:

        # Store its length in a variable
        num_chars = len(word)

        # If the length is not in dictionary
        if num_chars not in len_words:
            # Add it as key and the corresponding word as value
            len_words[num_chars] = [word]
        # If it's already in the dictionary
        else:
            # Add the corresponding word to its list value
            len_words[num_chars].append(word)

# Create an empty list to store len, words tuples
len_words_ls = []
for len, words in len_words.items():
    len_words_ls.append((len, words))

# Sort the list in descending order
len_words_ls.sort(reverse=True)

# Display the highest length with its list of words
len, words = len_words_ls[0]
print("Length:\t", len)
print("Words:\t", end="")
for word in words:
    print(word, end=" ")

# Close the file
fl.close()