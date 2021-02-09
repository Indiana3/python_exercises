##
# Compute the avarage of a collection of values
#

# Read the first value from the user
value = float(input("Please, enter the first value: "))

# Check the first value is not 0
if value == 0:
    print("The first value can't be 0")
    avarage = None
# Initialize the variables needed to compute the avarage of values
else:
    total = 0
    n_value = 0

# Compute and display the avarage of values 
while value != 0:
    total = total + value
    n_value = n_value + 1
    avarage = total / n_value
    value = float(input("Please, enter the next value: "))

# Display the avarange
if avarage != None:
    print("The avarage of this collection of values is", avarage)
