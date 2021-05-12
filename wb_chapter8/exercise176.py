## 
# Spell each letter of a word using NATO phonetic alphabet
#

## Convert a letter of a string in its corresponding word
# of the NATO phonetic alphabet
# @param s a string
# @return a concatenation of strings
def natoPhoneticAlphabet(s):
    nato_phonetic_alphabet = {"a": "Alpha", "b": "Bravo", "c": "Charlie", "d": "Delta",
    "e": "Echo", "f": "Foxtrot", "g": "Golf", "h": "Hotel", "i": "India", "j": "Juliet",
    "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o": "Oscar", "p": "Papa",
    "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango", "u": "Uniform", "v": "Victor",
    "w": "Whiskey", "x": "Xray", "y": "Yankee", "z": "Zulu"}
    # Base case
    if s == "":
        return ""
    # Recursive case
    else:
        return nato_phonetic_alphabet[s[0]] + " " + natoPhoneticAlphabet(s[1:len(s)])

# Read a word from user and display its phonetic spelling
def main():
    word = input("Please, enter a word: ")
    # Turn all the letters into lowercase
    word = word.lower()
    spelling = natoPhoneticAlphabet(word)
    print("The NATO phonetic spelling of '%s' is %s" % (word, spelling))

# Call the main function
if __name__ == "__main__":
    main()
