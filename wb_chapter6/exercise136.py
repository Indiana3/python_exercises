##
# Check if a value is in a dictionary
# Display the key/s that map to the provided value
#

## Find the keys (if any) of a value in a dictionary
# @param d the dictionary where to search for
# @param v the value you want to check
# return a list of keys that map to the provided value
#
def reverseLookup(d, v):
    keys = []
    for key in d:
        if d[key] == v:
            keys.append(key)
    return keys

# Create a dictionary and show how reverseLookup works
def main():
    # Read n key-value pairs from user
    d = {}
    key = input("Please, enter a key for your dictionary (blank to pass): ")
    while key != "":
        value = input("Please, enter the corresponding value: ")
        d[key] = value
        key = input("Please, enter a key for your dictionary (blank to pass): ")

    # Print the list of keys for different values passed as argument
    print(reverseLookup(d, "2"))
    print(reverseLookup(d, "3"))
    print(reverseLookup(d, ""))
    print(reverseLookup(d, "4"))

# Call the main function
if __name__ == "__main__":
    main()


