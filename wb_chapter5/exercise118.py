##
# Check if a string is a word by word palindrome
#
from exercise117 import wordsInAString

# Read a string from user
string = input("Please, enter a string: ")

# Remove punctuation marks from the string
words = wordsInAString(string)

# Store the elements of the list in reversed order
reversed_words = words[::-1]

# Print if the string entered is a word by word palindrome
for i in range(len(words)):
    if words[i] != reversed_words[i]:
        print("The string entered is not a word by word palindrome")
print("The string entered is a word by word palindrome")