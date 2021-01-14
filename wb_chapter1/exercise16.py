##
# Compute the area of a circle and the volume of a sphere
#
from math import pi

# Read the radius entered by users
r = float(input("Enter a radius: "))

# Compute the area and the volume
area = pi * r ** 2
volume = 4/3 * pi * r ** 3

# Display the output
print("The area of the circle with r =", r, "cm is %.2f" % area, "cm^2")
print("The volume of the sphere with r =", r, "cm is %.2f" % volume, "cm^3")
