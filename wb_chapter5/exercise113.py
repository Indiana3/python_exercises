##
# Read a collection of words and display each word only once
#

# Start with an empty list
words = []

# Read a word from user and add it to the list till a blank line is entered
word = input("Please, enter a word: ")
while word != "":
    words.append(word)
    word = input("Please, enter another word: ")

# Display each word in the list just once
for i in range(len(words)):
    if words[i] not in words[:i]:
        print(words[i])