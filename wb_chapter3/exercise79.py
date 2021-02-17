##
# Find the greatest common divisor of 2 positive integers n and m
#

# Read the 2 positive integers n and m
n = int(input("Please, enter the first positive integer: "))
m = int(input("Please, enter the second positive integer: "))

# Find the greatest common divisor
if n < m:
    d = n
else:
    d = m
while m % d != 0 or n % d != 0:
    d = d - 1

# Display the result
print("The greatest common divisor is {}".format(d))