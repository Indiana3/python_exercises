##
# Convert numbers from an arbitrary base to 10 base
# and viceversa
#
from exercise104bis import hex2int, int2hex

## Convert numbers from a base between 2 and 16 into a decimal
# @param n the number to convert
# @param b the base of n
# @return the corresponding decimal number
def b2decimal(n, b):
    # Initialize the decimal number equal to 0
    decimal = 0
    # Initialize the exponent equal to the higher position in the string number
    exp = len(n) - 1
    # Counter i starts counting from the first position of the string
    i = 0
    # Sum each digit of the string multiplied by the base powered by exponent
    while i < len(n):
        decimal += int(hex2int(n[i])) * b ** exp
        i += 1
        exp -= 1
    # Return the result
    return str(decimal)

## Convert numbers from a decimal into a base between 2 and 16
# @param n the number to convert
# @param b the new base
# @return the number in new base
def decimal2b(n, b):
    # Set quotient equal to the entered number
    q = int(n)
    # Set result as an empty string
    result = ""
    # Divide quotient by the base and put the rest in result
    r = q % b
    result = str(int2hex(r)) + result
    q = q // b
    # Do the same operation until quotient is greater than 0
    while q > 0:
        r = q % b
        result = str(int2hex(r)) + result
        q = q // b
    # Return result
    return result

# Read a base from the user
# Check if the base is in the range expected
# Read the number from the user
# If the base entered is 10, read the new base from the user
# and display the convertion
# If the base entered is not 10, convert and display number in 10 base
def main():
    base = int(input("Please, enter a base between 2 and 16: "))
    if base < 2 or base > 16:
        print("Sorry, you entered a base out of the expected range")
    else:
        num = input("Please, enter a number in {} base: ".format(base))
        if base == 10:
            new_base = int(input("Please, enter the new base you want to convert {} into: ".format(num)))
            if new_base < 2 or new_base > 16:
                print("Sorry, you entered a base out of the expected range")
            else:
                print("{} in {} base is {}".format(num, new_base, decimal2b(num, new_base)))
        else:
            print("{} in {} base is {} in 10 base".format(num, base, b2decimal(num, base)))

# Call the main function
main()







