##
# Convert a binary into a decimal number
#

# Read a binary number from the user
binary = input("Please, enter a binary number: ")

# Initialize decimal number to 0
decimal = 0
i = 0
j = len(binary) - 1

# Decimal number is equal to the sum of binary digits (dn) times their power of 2 (2n) 
while i <= len(binary) - 1:
    decimal = decimal + int(binary[i]) * 2 ** j
    i = i + 1
    j = j - 1

# Display decimal number    
print("{} in base 2 is {} in base 10".format(binary, decimal))