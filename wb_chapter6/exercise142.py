## Determine and display the number of unique characters
# in a string
#

# Read a string from user
string = input("Please, enter a string: ")
# Create a dictionary 
chars = {}
# Store each unique char of string as key
# and True as value for all keys
for char in string:
    chars[char] = True
# Display the number of keys in chars
print("In %s there are %i unique character/s" % (string, len(chars)))

