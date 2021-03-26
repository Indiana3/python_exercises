##
# Read a line of text and translate it to Pig Latin
# If a word begins with a consonant (including y),
# all the consonant up to the first vowel (excluding y)
# are moved and add to the end of the word followe by "ay"
# e.g. "computer" --> "omputercay"
#
# If a word begins with a vowel (not including y), 
# only "way" is added to the end of the word
# e.g. "algorithm" --> "algorithmway"
#

# Read a sentence from user
sentence = input("Please, enter the sentence you want to translate in Pig Latin: ")

# Create a consonant list
consonants = ["b", "c", "d", "f", "g", "h", "j", "k",
"l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x",
"y", "z"]

# Create a vowel list
vowels = ["a", "e", "i", "o", "u"]

# Create a list with all the words of the sentence as elements
words_in_sentence = sentence.split()

# Store the suffixes to add in constants
SUFFIX_FOR_CONSONANTS = "ay"
SUFFIX_FOR_VOWELS = "way"

# Set an empty list where storing Pig Latin words
pig_latin_words = []

# Translated each word into Pig Latin
# and store them in the list
for i in range(len(words_in_sentence)):
    word = list(words_in_sentence[i])
    if word[0] in consonants:
        while word[0] in consonants:
            beginning_consonant = word.pop(0)
            word.append(beginning_consonant)
        word.append(SUFFIX_FOR_CONSONANTS)
    elif word[0] in vowels:
        word.append(SUFFIX_FOR_VOWELS)
    word = "".join(word)
    pig_latin_words.append(word)

# Create a string with the words translated
sentence_translated = " ".join(pig_latin_words)

# Display the sentence translated
print(sentence_translated)

    
