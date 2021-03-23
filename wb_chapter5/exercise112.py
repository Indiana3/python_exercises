##
# From a list of values, create and display a new list 
# after removing the 2 largest and 2 smallest values
#

## Create a new list without the largest and the smallest values
# @param t a list of values
# @param n how many largest and smallest values have to be removed
# @return a new list without the removed elements
#
def remove_values(t, n):
    # Create a copy of the list passed with its elements in ascending order
    v = sorted(t)
    # Remove the first n values from list v
    v = v[n:]
    # Remove the last n values from list v
    v = v[:-n]
    return v

# From the list of values entered by the user, remove the 2 smallest and largest
# values using remove_values(t, n) function
def main():
    # Start with an empty list
    values = []
    # Read a value from user and add it to the list until he type enter
    value = input("Please, enter a value (blank to quit): ")
    while value != "":
        values.append(int(value))
        value = input("Please, enter a value (blank to quit): ")
    # Print an error message if values has less than 4 elements
    if len(values) < 4:
        print("Sorry, you entered less than 4 elements")
    else:
        # Store the list returned by remove_values() in a variable
        new_values = remove_values(values, 2)
        # Print the new list and the older list
        print(new_values)
        print(values)

# Call the main function
if __name__ == "__main__":
    main()