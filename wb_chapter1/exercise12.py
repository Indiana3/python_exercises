##
# Compute the distance in km between 2 points on earth
#

from math import radians, sin, cos, acos

# Read the latitude and longitude of 2 points entered by the users
t1 = float(input("Enter the latitude of first point: "))
g1 = float(input("Enter the longitude of first point: "))
t2 = float(input("Enter the latitude of second point: "))
g2 = float(input("Enter the longitude of second point: "))

# Convert degrees coordinates in radians coordinates
t1_rad = radians(t1)
g1_rad = radians(g1)
t2_rad = radians(t2)
g2_rad = radians(g2)

# Compute the distance between 2 points
distance = 6371.01 * acos(sin(t1_rad) * sin(t2_rad) + cos(t1_rad) * cos(t2_rad) * cos(g1_rad - g2_rad))

# Print the output
print("The distance between point with coordinates %.2f %.2f" % (t1, g1),
"and point with coordinates %.2f %.2f" % (t2, g2), "is %.2f" % distance)

