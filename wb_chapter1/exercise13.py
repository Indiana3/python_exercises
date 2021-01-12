##
# Change an amount of cents in pennies, nickels, dimes,
# quarters, loonies and toonies coins
#

# Read the number of cents from the users
cents = int(input("Enter the amount of cents you want ti change: "))

# Compute the change
toonies = cents / 200
cents = cents % 200
loonies = cents / 100
cents = cents % 100
quarters = cents / 25
cents = cents % 25
dimes = cents / 10
cents = cents % 10
nickels = cents / 5
pennies = cents % 5

# Display the output
print ("The amount of cents you entered can we change with:")
print ("%i toonies" % toonies)
print ("%i loonies" % loonies)
print ("%i quarters" % quarters)
print ("%i dimes" % dimes)
print ("%i nickels" % nickels)
print ("%i pennies" % pennies)