##
# Convert feet in inches, yards amd miles
#
IN_PER_FOOT = 12
YA_PER_FOOT = 0.333333
MI_PER_FOOT = 0.000189394

# Read the distance in feet from the users
feet = int(input("Enter the distance in feet: "))

# Convert in inches, yards and miles
inches = feet * IN_PER_FOOT
yards = feet * YA_PER_FOOT
miles = feet * MI_PER_FOOT

# Display the output
print(feet, "feet are", inches, "inches")
print(feet, "feet are", yards, "yards")
print(feet, "feet are", miles, "miles")