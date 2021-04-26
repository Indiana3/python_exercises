##
# Read 2 strings from user, determine if they are anagrams,
# display the result
#

## Count the occurencies of each character of a string
# @param s a string
# @return a dictionary 
#
def countOccurencies(s):
    # Store chars you want to remove in a list
    chars_to_remove = [" ", ",", ";", ":", ".", "?", "!"]
    # Remove these chars from s (if any)
    s = "".join(ch for ch in s if not ch in chars_to_remove)
    # Create a dictionary
    counter = {}
    # For each char of string, add it as key in dictionary
    # if not already stored and add 1 to its number of occurrencies
    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

# Read 2 strings from user 
def main():
    string1 = input("Please, enter the first string: ")
    string2 = input("Please, enter the second string: ")
    # Create 2 dictionaries with all the occurencies for
    # each unique character
    counter1 = countOccurencies(string1)
    counter2 = countOccurencies(string2)
    # Check if are anagrams and display the result
    if counter1 == counter2:
        print("%s and %s are anagrams" % (string1, string2))
    else:
        print("%s and %s aren't anagrams" % (string1, string2))

# Call the main function
if __name__ == "__main__":
    main()