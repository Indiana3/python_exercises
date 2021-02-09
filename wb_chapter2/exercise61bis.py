##
# Say if a license plate is valid
#

# Read a license plate string from the user
license_plate = input("Please, enter a valid license plate: ")

# Determine if the entered license plate is valid
if len(license_plate) == 6 and \
   license_plate[:3].isupper() and \
   license_plate[3:].isnumeric():
    style = "old"
elif len(license_plate) == 7 and \
     license_plate[:4].isnumeric() and \
     license_plate[4:].isupper():
      style = "new" 
else:
    style = None

# Display the result
if style == None:
    print("You entered an invalid string")
else:
    print("Valid for the", style, "style")