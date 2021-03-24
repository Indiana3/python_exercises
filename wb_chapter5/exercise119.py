##
# Read a series of values from the user,
# compute their avarage,
# print all the values before the avarage
# followed by the values equal to the avarage (if any)
# followed by the values above the avarage
#

# Start with an empty list
values = []

# Read values from user until blank line is entered
value = input("Please, enter a value: ")
while value != "":
    value = float(value)
    values.append(value)
    value = input("Please, enter another value: ")

# Compute the avarage of the values in the list
avarage = sum(values) / len(values)

# Create a list for values below the avarage
# followed by one for values equal to avarage
# followed by on for values above the avarage
below_avarage = []
equal_to_avarage = []
above_avarage = []

# For each value in values, determine if it's smaller, equal or greater than avarage
# and add it to the appropriate list
for i in range(len(values)):
    if values[i] < avarage:
        below_avarage.append(values[i])
    elif values[i] == avarage:
        equal_to_avarage.append(values[i])
    elif values[i] > avarage:
        above_avarage.append(values[i])

# Print below_avarage, equal_to_avarage and above avarage lists
print("Values below {} are:".format(avarage))
for value in below_avarage:
    print(" ", value)
print("Values equal to {} are:".format(avarage))
for value in equal_to_avarage:
    print(" ", value)
print("Values above {} are:".format(avarage))
for value in above_avarage:
    print(" ", value)