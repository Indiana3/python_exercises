##
# Using even parity, determine if parity bit should be 0 or 1
#

# Store the group of bits in a string as constant
GROUP_OF_BITS = 8

# Read the bit string from the user
bit_string = input("Please, enter a string of 8 bits (blank line to finish): ")

# For each string, determine whether is a valid bit string
while bit_string != "":
    if len(bit_string) != GROUP_OF_BITS:
        print("Bits in the string aren't 8")
    else:
        for i in range(GROUP_OF_BITS):
            if bit_string[i] != "0" and bit_string[i] != "1":
                print("You entered chars different from 0 or 1")
        # Determine the value of the parity bit
        # if 1 occurrences is even
        if bit_string.count("1") % 2 == 0:
            parity_bit = "0"
        # if 1 occurences is odd
        else:
            parity_bit = "1"
        # Display the parity bit
        print("Parity bit should be", parity_bit)
        
    # Ask for another bit string
    bit_string = input("Please, enter a new 8 bit string (blank line to finish): ")
            

            