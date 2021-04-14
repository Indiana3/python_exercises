##
# Display all the possible sublists of a list
#

## Compute all the sublists in a list of elements
# @param t a list
# @return all the possible sublists
#
def sublists(t):
    # Every list has a default empty list as sublist
    sublists = []
    sublists.append([])
    # Find all the sublists of the list
    for i in range(len(t)):
        for j in range(len(t), i, -1):
            sublists.append(t[i:j])
    return sublists

# Show the sublists of the following lists
def main():
    print(sublists(["casa", "albero", "giardino", "legnaia", "orto"]))
    print(sublists([1, 2, 3, 4, 5]))
    print(sublists([23.3, 12.1, 18.7, 90.2]))
    print(sublists(["studio", "lavoro", "amore", "relazioni", "sport", "meditazione", "hobbies"]))
    print([])
    print(["olistico"])

# Call the main function
if __name__ == "__main__":
    main()


