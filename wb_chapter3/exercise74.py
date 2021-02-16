##
# Implement Newton's method to compute the square root
# of an x number
#
GOOD_APPROXIMATION = 1e-12

# Read x from the user
x = float(input("Please, enter a number: "))

# Compute the good approximation
guess = x/2
while abs(guess ** 2 - x) > GOOD_APPROXIMATION:
    guess = (guess + x/guess) / 2

# Display the approximation with 4 decimal places
print("A good approximation of its square root is %.4f" % guess)


