## Modify a list by removing the first and the last elements
# @param t a list
# @return None
def chop(t):
    del t[0]
    del t[-1]
    return None

# Read a t list from user
# Modify the list by removing the first and the last elements
# Print what chop function returns
# Print t list
def main():
    t = []
    element = input("Please, enter a list element (blank to stop): ")
    while element != "":
        t.append(element)
        element = input("Please, enter a list element (blank to stop): ")
    print(chop(t))
    print(t)

# Call the main function
main()
