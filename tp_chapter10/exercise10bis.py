##
# Execute exercise 10 using bisect module
#
from exercise9 import list_builder
from bisect import bisect_left

def main():
    # Import the list of word to check
    t = list_builder('../tp_chapter8/words.txt')

    # Read a word from the user
    word = input("Please, type a word: ")

    # Determine the position the word checked would have in the sorted list
    i = bisect_left(t, word)
    
    # Check if the word entered is in the list
    if word == t[i]:
        print("%s is in the list" %word)
    else:
        print("%s is not in the list" %word)

# Call the main function
if __name__ == "__main__":
    main()

