##
# Compute the area of a triangle
#

# Read the base b and height h from the user
print("Please, enter: ")
b = float(input("the base of the triangle in cm: "))
h = float(input("the height of the triangle in cm: "))

# Compute the area
area = (b * h) / 2

# Display the result
print("The area of the triangle is %.2f cm^2" % area)