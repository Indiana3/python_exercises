##
# Prime Factors
#

# Read a positive integer (equal or more than 2)
n = int(input("Please, enter an integer (2 or greater): "))

factor = 2

# Check if the integer is equal or more than 2
if n < factor:
    print("You entered an integer smaller than 2")
else:
    print("The prime factors of {} are:".format(n))

# Compute and display the prime factors
while factor <= n:
    if n % factor == 0:
        print("{}".format(factor))
        n = n//factor
    else:
        factor = factor + 1
