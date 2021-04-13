##
# Check if a list is a sublist of another list
#

## Check if a list is a sublist of another list
# @param larger the list with a greater number of elements
# @param smaller the list with a lower number of elements
# @return True if one of the 2 lists is a sublist; False otherwise
#
def isSublist(larger, smaller):
    # The empty list and the whole list are always
    # sublists of any list
    if smaller == [] or larger == smaller:
        return True
    # In the other cases, check if the first element of smaller is in larger
    if smaller[0] in larger:
        # Determine the position of this element in larger
        # and store its value
        check_index = larger.index(smaller[0])
        # All the following elements of smaller must be in larger
        # and must be adjacent
        for i in range(1, len(smaller)):
            # For each element, increase the check index by one 
            check_index += 1
            if smaller[i] in larger \
                and larger.index(smaller[i]) == check_index:
                    continue 
            return False
        return True

# Read 2 lists from user and determine if one is
# a sublist of the other
def main():
    # First list
    list1 = []
    item = input("Please, enter an item (blank to skip at the second list): ")
    while item != "":
        list1.append(item)
        item = input("Please, enter another item (blank to skip at the second list): ")
    # Second list
    list2 = []
    item = input("Please, enter an item (blank to move one): ")
    while item != "":
        list2.append(item)
        item = input("Please, enter another item (blank to move on): ")
    # Determine which list has the greater number of elements
    if len(list1) >= len(list2):
        larger = list1[:]
        smaller = list2[:]
    elif len(list1) < len(list2):
        larger = list2[:]
        smaller = list1[:]
    # Print if smaller is a sublist of larger
    if isSublist(larger, smaller):
        print(smaller, "is a sublist of", larger )
    else:
        print(smaller, "is not a sublist of", larger)

# Call the main function
if __name__ == "__main__":
    main()

