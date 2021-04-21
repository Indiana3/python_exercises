##
# Read a message from the user
# and display the corresponding key presses needed
# to generate it
#

# Create a dictionary that maps from each letter/symbol
# to the key presses
key_presses = {".": 1, ",": 11, "?": 111, "!": 1111, ":": 11111,
"a": 2, "b": 22, "c": 222, "d": 3, "e": 33, "f": 333, "g": 4, "h": 44,
"i": 444, "j": 5, "k": 55, "l": 555, "m": 6, "n": 66, "o": 666, "p": 7,
"q": 77, "r": 777, "s": 7777, "t": 8, "u": 88, "v": 888, "w": 9, "x": 99,
"y": 999, "z": 9999, " ": 0}

# Read a message from user and convert all characters
# to lowercase (if any)
message = input("Please, enter a message: ")
message = message.lower()

# For each char of message, print its corresponding key presses
for c in message:
    print(key_presses[c], end="")
print()