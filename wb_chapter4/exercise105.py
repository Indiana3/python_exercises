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
    q = n
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








