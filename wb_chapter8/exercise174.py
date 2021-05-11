##
# Compute the greatest common divisor of 2 positive integers
#

## Compute the greatest common divisor of 2 positive integers
# @param a the first positive integer
# @param b the second positive integer
# @return the greatest common divisor
#
def greatestCommonDivisor(a, b):
    # Base case
    if b == 0:
        return a
    # Recursive case
    c = a % b
    return greatestCommonDivisor(b, c)

# Read 2 positive integers from user
# Display the greatest common divisor
def main():
    a = int(input("Please, enter a positive integer: "))
    b = int(input("Please, enter another positive integer: "))
    divisor = greatestCommonDivisor(a, b)
    print("The greatest common divisor of %d and %d is %d" % (a, b, divisor))

# Call the main function
if __name__ == "__main__":
    main()