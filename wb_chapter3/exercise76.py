##
# Check if a string is a palindrome
#

# Read a string from the user
s = input("Please, enter a string: ")

# Convert all chars from uppercase to lowercase (if necessary)
lowercase_s = s.lower()

# Remove spacing and punctuation marks from the string
clean_s = lowercase_s.translate({ord(c): None for c in " ,;.:?!" })

# Determine the reverse of the string
r = clean_s[::-1]

# Initialize a counter to 0 to traverse the reverse string
i = 0

# Think as if the string entered is a palindrome
is_palindrome = True

# Determine if the string is a palindrome
for c in clean_s:
    if c != r[i]:
        is_palindrome = False
        break
    else:
        i = i + 1

# Display an appropriate output message
if is_palindrome:
    print("The string %s is a palindrome" % s)
else:
    print("The string %s is not a palindrome" % s)