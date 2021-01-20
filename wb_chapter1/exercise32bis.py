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
i = 0
while i < len(int_str) - 1:   
    print(int_str[i], "+", end=" ")
    i = i + 1
if i == len(int_str) - 1:
    print(int_str[i], "=", total)

