##
# Compute the area of a triangle with all the 3 sides known
#
from math import sqrt

# Read the lengths of sides
print("Please, enter: ")
s1 = float(input("the length of first side in cm: "))
s2 = float(input("the length of second side in cm: "))
s3 = float(input("the length of third side in cm: "))

# Compute the area
s = (s1 + s2 + s3) / 2
sq_area = s * (s - s1) * (s - s2) * (s - s3)

if sq_area < 0:
    print("Error: the rooting is a negative number")
    quit()

area = sqrt(sq_area)

# Display the area
print("The area of the triangle measures %.2f cm^2" % area)