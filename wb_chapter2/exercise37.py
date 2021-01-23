##
# Display whether a letter is a vowel, semi-vowel or consonant
#

# Read the letter
letter = input("Please, enter a letter: ")

# Determine whether the letter is a vowel, semi-vowel or consonant
if letter == "a" or letter == "e" or \
    letter == "i" or \
    letter == "o" or letter == "u":
    print("The entered letter is a vowel")
elif letter == "y":
    print("The entered letter is a semi-vowel")
else:
    print("The entered letter is a consonant")