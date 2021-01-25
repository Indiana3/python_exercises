##
# Determine the name of a shape from its number of sides
#

# Read the number of sides
sides = int(input("Please, enter a number of sides: "))

# Find the appropriate name of the shape if sides is >= 3 and <= 10
name = ""
if sides == 3:
    name = "triangle"
elif sides == 4:
    name = "square"
elif sides == 5:
    name = "pentagon"
elif sides == 6:
    name = "esagon"
elif sides == 7:
    name = "eptagon"
elif sides == 8:
    name = "octagon"
elif sides == 9:
    name = "nonagon"
elif sides == 10:
    name = "decagon"

# Display the message error if sides is not in the established range
if name == "":
    print("Please, enter a number from 3 up to (and including) 10 sides")
else:
    print("That's a", name)