##
# Convert a non negative integer into a binary number
#

## Convert a decimal number to its binary representation
# @param n a decimal number
# @return its binary representation
#
def decimalToBinary(n):
    # Base case
    if n == 0:
        return str(0)
    if n == 1:
        return str(1)
    # Recursive case
    return decimalToBinary(n//2) + str(n % 2)

# Read a non negative number from user and print its
# binary representation
def main():
    num = int(input("Please, enter a non negative number: "))
    if num < 0:
        raise Exception("Only positive integers, please")
    binary = decimalToBinary(num)
    print("Binary representation of %d is %s" % (num, binary))


# Call the main function
if __name__ == "__main__":
    main()

