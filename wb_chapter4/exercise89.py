##
# Convert an integer to its ordinal number
#

## Convert an integer from 1 to 12 in its ordinal number
# @param n the integer converted
# @return the corrisponding ordinal number if n > 1 and n < 12
# @ return an empty string if n < 1 or n > 12
#

def to_ordinal_num(n):
    if n < 1 or n > 12:
        return ""
    else:
        if n == 1:
            return "first"
        elif n == 2:
            return "second"
        elif n == 3:
            return "third"
        elif n == 4:
            return "fourth"
        elif n == 5:
            return "fifth"
        elif n == 6:
            return "sexth"
        elif n == 7:
            return "seventh"
        elif n == 8:
            return "eighth"
        elif n == 9:
            return "nineth"
        elif n == 10:
            return "tenth"
        elif n == 11:
            return "eleventh"
        elif n == 12:
            return "twelfth"

# Read the integer from the user and display its ordinal
def main():
    n = int(input("Please, enter a number between 1 and 12: "))
    print("The ordinal number of %i is %s" % (n, to_ordinal_num(n)))

# Call the main function
if __name__ == "__main__":
    main()
