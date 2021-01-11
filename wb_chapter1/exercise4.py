##
# Compute the area of a field in acres
#

SQFT_PER_ACRE = 43560

# Takes the length and width from the users
length = float(input("Insert the length of the field in feet: "))
width = float(input("Insert the length of the field in feet: "))

# Compute the area in acres
area = length * width / SQFT_PER_ACRE

#Display the output
print("The field area is %.2f acres" % area)