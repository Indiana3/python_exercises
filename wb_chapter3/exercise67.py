##
# Compute the perimeter of a polygon
#
from math import sqrt

# Read the first coordinates (x; y) from the user
x = input("Enter the first x-coordinate: ")
y = input("Enter the first y-coordinate: ")

# Initialize number of entered points equal to 1
# Initialize perimeter equal to 0
# Store the first coordinates in appropriate variable to compute
# the last side of the polygon
# x_prev and y_prev are the coordinates of the previous point
# needed to compute the length of each side
n_points = 1
perimeter = 0
x1 = int(x)
y1 = int(y)
x_prev = int(x1)
y_prev = int(y1)

# Compute the length of each side of the polygon
while True:
    x = int(x)
    y = int(y)
    side = sqrt(abs(x_prev - x) ** 2 + abs(y_prev - y) ** 2)

# Add each side to perimeter
    perimeter += side
    x_prev = x
    y_prev = y

    x = input("Enter the next x-coordinate (blank to quit): ")
    if x != "":
        y = input("Enter the next y-coordinate: ")
        n_points = n_points + 1
    else:
        break

# Check number of points
if n_points >= 3:
    # Compute last side using the coordinates of the first point (x1; y1)
    # Add last side to perimeter
    last_side = side = sqrt(abs(x_prev - x1) ** 2 + abs(y_prev - y1) ** 2)
    perimeter = perimeter + last_side
else:
    perimeter = None

# Display the perimeter
if perimeter:
    print("The perimeter of the polygon is %.2f" % perimeter)
else:
    print("You entered less than 3 points")