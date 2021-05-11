##
# Read values from users until a blank line is entered
# Sum the values using recursive function
#

## Sum values entered by user
# @param None
# @return the summation of values entered
#
def recursive_sum():
    line = input("Please, enter a value: ")
    # Base case
    if line == "":
        return 0.0
    # Recursive case
    total = float(line) + recursive_sum()
    return total

# Call recursive sum and display the result
def main():
    total = recursive_sum()
    print("The summation of values entered is %.1f" % total)

# Call the main function
if __name__ == "__main__":
    main()