##
# Compute the median value of three numbers
#

## Compute the median value of three numbers using if-elif statements
# @parameter value1 the first of the 3 numbers
# @parameter value2 the second of the 3 numbers
# @parametre value3 the third of the 3 numbers
# @return the median value of value1, value2 and value3
#

def median_value(value1, value2, value3):
    if value1 < value2 and value1 > value3 or \
        value1 > value2 and value1 < value3:
        median_value = value1
    elif value2 < value1 and value2 > value3 or \
        value2 > value1 and value2 < value3:
        median_value = value2
    elif value3 > value1 and value3 < value2 or \
        value3 < value1 and value3 > value2:
        median_value = value3
    return median_value

# Display the median of the three values entered by the user
def main():
    value1 = float(input("Please, enter the first value: "))
    value2 = float(input("Please, enter the second value: "))
    value3 = float(input("Please, enter the third value: "))

    print("Median value before %.2f %.2f and %.2f is %.2f" \
        % (value1, value2, value3, median_value(value1, value2, value3)))

# Call the main function
main()    
