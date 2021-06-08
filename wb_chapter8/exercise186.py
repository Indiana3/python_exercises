## Compress a string or list
# @param t a string or a list
# @return a compressed string or list
#
def compression(t):
    # Base Case
    if len(t) == 0:
        return []
    
    # Recursive Case
    i = 0
    occurences = 1
    
    # Check if the adjacent char is equal to the previous one
    while t[i:i+1] == t[i+1:i+2]:
        occurences += 1
        # The new list starts from the adjacent char
        t = t[i+1:]
    
    # Store the char and its occurences in a lsit
    compressed = [t[i], occurences]
    
    # The new list starts from the adjacent char
    t = t[i+1:]
    return compressed + compression(t)

# Scope the main program inside a main function
def main():
    # Create a list to store data entered from the user
    ls = []
    
    # Read an element from the user and add it to ls
    elem = input("Please, enter an element (blank to move on): ")
    while elem != "":
        ls.append(elem)
        elem = input("Please, enter an element (blank to move on): ")

    # Display the compressed list
    comp_ls = compression(ls)
    print(comp_ls)

# Call the main function
if __name__ == "__main__":
    main()
