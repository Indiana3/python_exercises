##
# Convert a Roman value to its integer
#

## Convert a Roman value to its integer
# @param s a string representing a Roman value
# @return an integer
#
def romanToInteger(s):
    # Base case
    if s == "":
        return 0
    # Recursive case
    if s[0] == "I":
        arabic = 1
    if s[0] == "V":
        arabic = 5
    if s[0] == "X":
        arabic = 10
    if s[0] == "L":
        arabic = 50
    if s[0] == "C":
        arabic = 100
    if s[0] == "D":
        arabic = 500
    if s[0] == "M":
        arabic = 1000
    # Check if a smaller value precedes a larger value;
    # if so, subtract it from the larger value
    if s[0:2] == "IV" or s[0:2] == "IX":
        arabic = -1
    if s[0:2] == "XL" or s[0:2] == "XC": 
        arabic = -10
    if s[0:2] == "CD" or s[0:2] == "CM":
        arabic = -100
    return arabic + romanToInteger(s[1:len(s)])

# Read a Roman value from user and display its corresponding integer
def main():
    num = input("Please, enter a Roman value: ")
    arabic = romanToInteger(num)
    print("The corresponding integer to %s is %d" % (num, arabic))

# Call the main function
if __name__ == "__main__":
    main()