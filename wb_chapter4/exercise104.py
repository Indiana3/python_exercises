##
# Convert hexadecimal into decimal digits and viceversa
#

## Convert a string with a single hexadecimal digit into a base 10 integer
# @param s a single hexadecimal digit from 0 to F
# @return the corresponding base 10 integer;
# False if s is outside the expected range
def hex2int(s):
    s = s.lower()
    if s >= "0" and s <= "9":
        return int(s) 
    elif s >= "a" and s <= "f":
        if s == "a":
            return 10
        elif s == "b":
            return 11
        elif s == "c":
            return 12
        elif s == "d":
            return 13
        elif s == "e":
            return 14
        elif s == "f":
            return 15
    else:
        print("The digit you entered is not in the expected range")
        quit()

## Convert an integer into a single hexadecimal digit 10
# @param n an integer between 0 and 15
# @return the corresponding hexadecimal digit;
# False if s is outside the expected range
def int2hex(n):
    if n < 0 or n > 15:
        print("The digit you entered is not in the expected range")
        quit()
    elif n >= 0 and n <= 9:
        return str(n)
    elif n >= 10 and n <= 15:
        if n == 10:
            return "a"
        elif n == 11:
            return "b"
        elif n == 12:
            return "c"
        elif n == 13:
            return "d"
        elif n == 14:
            return "e"
        elif n == 15:
            return "f"



