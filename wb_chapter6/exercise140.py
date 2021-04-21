##
# Read a postal code from user
# and display province/territory associated with it
#

# Read the postal code from user
postal_code = input("Please, enter a valid postal code: ")

# Check if the first char is a valid
if postal_code[0] in ["D", "F", "I", "O", "Q", "U", "W", "Z"]:
    print("Error: Invalid postcode")
else:
    # Check if the second char is a digit
    # If so, check if the adress is rural or urban
    if postal_code[1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Error: Invalid postcode")
    else:
        if postal_code[1] == "0":
            adress = "rural"
        else:
            adress = "urban"
        # Build a dictionary with the valid letters as keys
        # and province/territory as values
        provinces = {
            "A": "Newfoundland",
            "B": "Nova Scotia",
            "C": "Prince Edward Island",
            "E": "New Brunswick",
            "G": "Quebec",
            "H": "Quebec",
            "J": "Quebec",
            "K": "Ontario",
            "L": "Ontario",
            "M": "Ontario",
            "N": "Ontario",
            "P": "Ontario",
            "R": "Manitoba",
            "S": "Saskatchewan",
            "T": "Alberta",
            "V": "British Columbia",
            "X": "Nunavut or Northwest Territories",
            "Y": "Yukon"
        }
        # Display the province/territory associated with
        # the first char and if the adress is rural or urban
        print("The postal code is for a/an %s adress in %s " % (adress, provinces[postal_code[0]]))
    
        