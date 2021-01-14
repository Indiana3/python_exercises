##
# Convert height entered in feet and inches into centimeters
#
IN_PER_FT = 12
CM_PER_INCH = 2.54

# Read a number of feet and a number of inches from users
print("Please, enter yout height: ")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))

# Compute the equivalent in centimeters
cm = (feet * IN_PER_FT + inches) * CM_PER_INCH

# Display the output
print("Your height is", cm, "cm")
