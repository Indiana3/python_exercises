##
# Classify a triangle from the length of its sides
#

# Read the length of its sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Classify the triangle
if side1 == side2 == side3:
    triangle = "equilateral"
elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle = "isosceles"
else:
    triangle = "scalene"

# Display the result
print("The triangle is", triangle)