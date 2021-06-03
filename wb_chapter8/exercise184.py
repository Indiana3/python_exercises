##
# Flatten lists
#

## Flatten a list that has nested lists as elements
# @param t a list
# @return a flattened list
#
def flattenAList(t):
    if len(t) == 0:
        return t
    if type(t[0]) == type(t):
        l1 = flattenAList(t[0])
        l2 = flattenAList(t[1:])
        return l1 + l2
    if type(t[0]) != type(t):
        l1 = [t[0]]
        l2 = flattenAList(t[1:])
        return l1 + l2

# Demonstrate the flattenAList function inside a main function
def main():
    
    # Flatten an empty list
    empty = flattenAList([])
    
    # Flatten nested lists
    little_nested = flattenAList([1, 2, 3, [4, 6,], "gallo"])
    nested = flattenAList([1, 2, ["ciao", "pippo", ["giornale"]], 7])
    super_nested = flattenAList(["ciao", [1, 2, 3], ["p", "i", ["ora", [4, 5, 6, []]]]])

    # Print the flattened lists
    print(empty)
    print(little_nested)
    print(nested)
    print(super_nested)

# Call the main function
if __name__ == "__main__":
    main()
