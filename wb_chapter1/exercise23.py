##
# Compute the area of a regular polygon
#

from math import pi, tan

# Read the length of a side s and the number of sides n
print("Please, enter: ")
s = float(input("the length of a side in cm: "))
n = int(input("the number of sides: "))

# Compute the area
area = (n * s ** 2) / (4 * tan(pi/n))

# Display the result
print("The area measures % .2f cm^2" % area)
