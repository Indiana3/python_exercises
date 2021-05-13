##
# Demonstrate squareRoot() by computing square roots
# of different values
#

## Compute the square root of a number
# @param n the number square root is computed for
# @param guess the approximation of square root
# @return the square root with its best approximation
#
def squareRoot(n, guess=1.0):
    # Base case
    if abs(guess**2-n) < 1e-12:
        return guess
    # Recursive case
    return squareRoot(n, (guess + n/guess)/2)

# Create a list with some values
values = [2, 3, 2.3, 67, 8.5]
# Compute square root of each previous value
# using  squareRoot function
for value in values:
    print(squareRoot(value))
