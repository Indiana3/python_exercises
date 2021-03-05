##
# Reduce a fraction to its lowest terms
#

## Reduce a fraction to lowest terms
# @param n numerator
# @param d denominator
# @return n and d of the reduced fraction
def fractionToLowestTerms(numerator, denominator):
    if numerator > denominator:
        max_divisor = denominator
    else:
        max_divisor = numerator
    # Find the greatest common divisor between numerator and denominator
    while numerator % max_divisor != 0 or \
        denominator % max_divisor != 0:
        max_divisor = max_divisor - 1
    # Reduce both numerator and denominator to lowest terms
    numerator = numerator // max_divisor
    denominator = denominator // max_divisor
    # Return the reduced numerator and denominator
    return numerator, denominator

# Read a numerator and denominator from the user
# Display the fraction with numerator and denominator reduced
def main():
    numerator = int(input("Please, enter a numerator: "))
    denominator = int(input("Please, enter a denominator: "))
    numerator, denominator = fractionToLowestTerms(numerator, denominator)
    print("The reduced fraction has {} as numerator and {} as denominator".format(numerator, denominator))

# Call the main function
main()