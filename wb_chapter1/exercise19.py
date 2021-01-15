##
# Compute the final speed of an object dropped by a known
# height
#
from math import sqrt

# Define the gravity acceleration constant in m/s ** 2
GRAVITY_CONST = 9.8

# Read the height in meters from which the object is dropped
h = float(input("Enter the height from which" \
    " the object is dropped in meters: "))

# Compute the object speed when it hits the ground
final_speed = sqrt(2 * GRAVITY_CONST * h)

# Display the result
print("The final speed at which the object hits the ground" \
    " is %.2f m/s" % final_speed)