##
# Capitalize letters in a string typed uncorrectly
#

## Capitalize all the letters typed uncorrectly
# @param s a string
# @return the string with the letters capitilized correctly
#
def capitilizeString(s):
    # Create an empty string where adding 
    # each character of s, capitilized or not capitilized
    cap_char_s = ""
    
    # Set the position of chars in s equal to 0
    position = 0

    # Check each character in s
    while position < len(s):

        # Capitilize the first non-space character in s
        # Capitilize the first non-space character after ".", "!", "?"
        # Capitilize "i" if preceded by " " and followed by " ", "!", "?", "'"
        if position == 0 or \
            s[position-2] == "." and s[position-1] == " " or \
            s[position-2] == "!" and s[position-1] == " " or \
            s[position-2] == "?" and s[position-1] == " " or \
            s[position] == "i" and s[position-1] == " " or \
            s[position] == " " and s[position-1] == "i" or \
            s[position] == "." and s[position-1] == "i" or \
            s[position] == "!" and s[position-1] == "i" or \
            s[position] == "?" and s[position-1] == "i" or \
            s[position] == "'" and s[position-1] == "i":
                cap_char_s += s[position].upper()
        else:
            # Add the lowercase character
            cap_char_s += s[position]
        
        # Move position in s
        position = position + 1
    
    return cap_char_s

# Read a string from the user
def main():
    s = input("Please, type any string you want: ")
    
    # Display the capitilize string calling capitilizeString function
    print(capitilizeString(s))

# Call the main function
main()


