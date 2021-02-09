##
# Say if a license plate is valid
#

# Read a license plate string from the user
license_plate = input("Please, enter a valid license plate: ")

# Determine if the entered license plate is valid
if len(license_plate) == 6:
    if license_plate[:3].isupper():
        if license_plate[3:].isnumeric():
            style = "old"
        else:
            style = None
    else:
        style = None
elif len(license_plate) == 7:
    if license_plate[:4].isnumeric():
        if license_plate[4:].isupper():
            style = "new"
        else:
            style = None
    else:
        style = None 
else:
    style = None

# Display the result
if style == None:
    print("You entered an invalid string")
else:
    print("Valid for the", style, "style")