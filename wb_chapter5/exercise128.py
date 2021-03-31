# Determine the number of elements in a list greater than
# or equal to a minimum value and lower than a maximum value
# 

## Determine the number of elements in a list that are
# greater than or equal a min value and less than
# a max value
# @param t a list of value
# @param min a minimum value
# @param max a maximum value
# @return an integer greater than or equal to 0
#
def countRange(t, min, max):
    counter = 0
    for i in range(len(t)):
        if t[i] >= min and t[i] < max:
            counter += 1
    return counter

# Store some values in a list and determine how many values
# are greater than or equal to a min value and less than
# a maximum value
def main():
    values = []
    # Read a value from user until a blank string is entered
    num = input("Please, enter a number (blank to stop): ")
    while num != "":
        # Add num to values
        values.append(float(num))
        num = input("Please, enter a number (blank to stop): ")
    # Enter a minimum value
    min_value = float(input("Please, enter a minimum value: "))
    # Enter a maximum value
    max_value = float(input("Please, enter a maximum value: "))
    # Check how many elements in the list are greter than or equal to min_value
    # and less than max_value
    counter = countRange(values, min_value, max_value)
    # Display the occurrences
    print("There are %i elements between %.2f and %.2f" %(counter, min_value, max_value))

# Call the main function
if __name__ == "__main__":
    main()
