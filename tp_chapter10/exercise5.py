## Check if the list is sorted in ascending order
# @param t a list
# @return True if the list elements are sorted in ascending order;
# False otherwise
def is_sorted(t):
    # Duplicate the list in ascending order
    t1 = sorted(t)
    if t == t1:
        return True
    return False
   
def main():
    # Read a list from the user
    t = []
    element = input("Please, add an element to the list ( blank to stop): ")
    while element != "":
        t.append(element)
        element = input("Please, add an element to the list ( blank to stop): ")
    # Check if the elements are sorted in ascending order
    # Display the result
    if is_sorted(t):
        print("The elements are sorted in ascending order")
    else:
        print("The elements aren't sorted in ascending order")

# Call the main function
main()