##
# Convert hexadecimal into decimal digits and viceversa
#

## Convert a string with a single hexadecimal digit into a base 10 integer
# @param s a single hexadecimal digit from 0 to F
# @return the corresponding base 10 integer;
# False if s is outside the expected range
def hex2int(s):
    s = s.lower()
    hexadecimal_digits = "0123456789abcdef"
    i = 0
    while i < len(hexadecimal_digits):
        if s == hexadecimal_digits[i]:
            return i
        i = i + 1
    return -1

## Convert an integer into a single hexadecimal digit 10
# @param n an integer between 0 and 15
# @return the corresponding hexadecimal digit;
# False if s is outside the expected range
def int2hex(n):
    hexadecimal_digits = "0123456789abcdef"
    if n >= 0 and n <= 15:
        return hexadecimal_digits[n]
    else:
        return -1

# Read an hexadecimal digit and an integer between 0 and 15
# Display the result or an appropriate message of error
# if the parameter is out the expected range
def main():
    s = input("Please, enter an hexadecimal digit: ")
    n = int(input("Please, enter an integer: "))
    if hex2int(s) == -1 or int2hex(n) == -1:
        print("You entered a digit out of the expected range")
    else:
        print("Hex {} --> int {}". format(s, hex2int(s)))
        print("Int {} --> hex {}". format(n, int2hex(n)))

# Call the main function
main()
    


        