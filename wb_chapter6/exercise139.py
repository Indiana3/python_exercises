##
# Translate a string of letters and number in Morse code
#

# In a dictionary, store each letter/number as key and its Morse code as value
morse_code = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
"e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
"k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
"q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-",
"w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----",
"2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
"8": "---..", "9": "----."}

# Read a message from user 
message = input("Please, enter a message: ")

# Turn all chars to lowercase (if any)
message = message.lower()

# Print message in Morse code
for c in message:
    print(morse_code[c], end=" ")
print()