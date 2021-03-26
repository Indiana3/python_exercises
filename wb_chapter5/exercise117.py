##
# Read a string and display the words it is made of with
#

## Remove the punctuation marks (",", ".", "?", "-", "'", "!", ":", ";") 
# from a string 
# @param s a string
# @return a list of the words in the string without punctuation marks
#
def wordsInAString(s):
    # Set empty the list containing the words in the string 
    words = []
    # Store the punctuation marks to check in a list
    punctuation_marks = [",", ".", "?", "-", "'", "!", ":", ";"]
    # For each word of the string, check if it has a punctuation mark at the end of it
    string_splitted = s.split()
    for i in range(len(string_splitted)):
        # Consider each character of the word separately
        word_splitted = list(string_splitted[i])

        # Remove the punctuation mark if and while it is the first element of the list
        while len(word_splitted) > 0:
            if word_splitted[0] in punctuation_marks:
                word_splitted.pop(0)
        
        # Execute only if word_splitted is not empty
        if len(word_splitted) != 0:

            # Remove the punctuation mark if and while it is the last element of the list
            while word_splitted[-1] in punctuation_marks:
                word_splitted.pop()
            
            # Restore the word with no punctuation mark
            word = "".join(word_splitted)
            # And add it to the list
            words.append(word)
    return words

# Read a string from user and display the words is made of with
def main():
    string = input("Please, enter a string: ")
    print("The string '{}' is made of: ".format(string))
    for word in wordsInAString(string):
        print(" ", word)

# Call the main function
if __name__ == "__main__":
    main()




