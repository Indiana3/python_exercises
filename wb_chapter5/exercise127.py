##
# Determine if a list of values is sorted
#

## Determine if a list of values is sorted
# @param t a list of values
# @return True if the list is sorted; False otherwise
#
def isAListSorted(values):
    if len(values) == 0:
        return True
    elif len(values) == 1:
        return True
    else:
        is_ascending = True
        # Check if the values are in ascending order
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                is_ascending = False
                break
        if is_ascending:
            return True
        # Check if the values are in descending order
        for i in range(len(values)-1):
            if values[i] < values[i+1]:
                return False
        return True

# Read a collection of values from user
def main():
    values = []
    value = input("Please, enter a value (blank to stop): ")
    while value != "":
        values.append(float(value))
        value = input("Please, enter another value (blank to stop): ")
    # Report if the values in the list are sorted or not
    if isAListSorted(values):
        print("The values are sorted")
    else:
        print("Tha values are not sorted")

# Call the main function
if __name__ == "__main__":
    main()
