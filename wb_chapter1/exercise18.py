##
# Compute the volume of a cylinder
#
from math import pi

# Read the radius and the height from the user
r = float(input("Enter the radius in cm: "))
h = float(input("Enter the height in cm: "))

# Compute the volume
volume = pi * r ** 2 * h

# Display the volume
print("The volume of cylinder measures %.1f cm^3" % volume)