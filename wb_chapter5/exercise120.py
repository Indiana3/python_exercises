##
# Read a sequence of items, add them in a list,
# format the list, display the result as a string
#

## Format a list, separating each item with a comma and
# including "and" before the last one
# @param t a list 
# @return a string with all the items of the list formatted
#
def listFormatter(t):
    # if t has one element, return it as string
    if len(t) == 0:
        s = "<empty>"
    # if t has one element, return it as string
    elif len(t) == 1:
        s = t[0]
    # if t has more than 1 element
    else:
        # Create a sublist with all elements but the last
        v = t[:-1]
        # Create a string so that each element is separated by commas
        v = ", ".join(v)
        # Create a second sublist with "and" and last element of t
        p = ["and", t[-1]]
        # Create a string so that the last element is preceded by "and"
        p = " ".join(p)
        # Concatenate the 2 strings
        s = v + " " + p
    return s

# Read a list of items from the user till a blank line is entered
# Display the list formatted as a string using listFormatter function
def main():
    items = []
    item = input("Please, enter a string: ")
    while item != "":
        items.append(item)
        item = input("Please, enter another string: ")
    print("Here the list formatted: ")
    print(" '{}'".format(listFormatter(items)))

# Call the main function
if __name__ == "__main__":
    main()