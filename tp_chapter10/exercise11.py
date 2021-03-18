##
# Check how many reverse pairs there are in a word list
#
from exercise9 import list_builder
from bisect import bisect_left

def main():
    # Import the list of word to check
    t = list_builder('../tp_chapter8/words.txt')

    # For each string element, compute its reverse
    for i in range(len(t)):
        word = t[i]
        reversed_word = word[::-1]
    # Check if the reversed string is in the list t
    # If it is, print the string element and the reversed string
        j = bisect_left(t, reversed_word)
        if j != len(t) and reversed_word == t[j]:
            print(word)
            print(reversed_word)

# Call the main function
if __name__ == "__main__":
    main()





