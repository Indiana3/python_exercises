##
# Show Python's arithmetical operators
#

from math import log10

# Read the 2 integers a anb b from users
a = int(input("Enter the first integer number: "))
b = int(input("Enter the second integer number: "))

# Print the results of the following arithmatic operations:sum, subtraction, moltiplication,
# division, reminder, logarithm, power
print(a, "+", b, "is", a+b)
print(a, "-", b, "is", a-b)
print(a, "*", b, "is", a*b)
print(a, "/", b, "is", a/b)
print(a, "%", b, "is", a%b)
print(a, "log10", b, "is", log10(a))
print(a, "^", b, "is", a**b)