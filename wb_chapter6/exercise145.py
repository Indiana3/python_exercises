##
# Compute the score of a word according to the game of Scrabble
#

# Create a dictionary that maps from letters to point values
scrabble = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4,
"i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
"s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

# Read a word from user
word = input("Please, enter a word: ")

# Create a score variable and set it equal to 0
score = 0
# For each letter, compute the score and add it to score variable
lowercase = word.lower()
for ch in lowercase:
    score += scrabble[ch]

# Display score
print("%s is worth %i points" % (word, score))
