##
# Check if a string is a palindrome
#

# Read a string from the user
s = input("Please, enter a string: ")

# Determine the reverse of the string
r = s[::-1]

# Initialize a counter to 0 to traverse the reverse string
i = 0

# Determine if the string is a palindrome
for c in s:
    if c != r[i]:
        is_palindrome = False
        break
    else:
        i = i + 1

# The string is a palindrome
is_palindrome = True

# Display an appropriate output message
if is_palindrome:
    print("The string %s is a palindrome" % s)
else:
    print("The string %s is not a palindrome" % s)