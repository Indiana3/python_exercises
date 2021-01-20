##
# Compute the sum of the digits in an integer
#

# Read the four-digit integer
int_str = input("Please, enter a four-digit integer: ")

# Compute the sum of the four digits
total = 0
for c in int_str:
    total += int(c)

# Display the sum of the digits 
print(int_str[0], "+", int_str[1], end = " ")
print("+", int_str[2], "+", int_str[3], end=" ")
print("=", total)