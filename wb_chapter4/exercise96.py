##
# Determine if a string represents an integer or not
#

## Check if a string is an integer string
# @param s a string
# @return True if s is an integer string, otherwise return False
# 
def isInteger(s):
    char_in_integer_string = "+-0123456789"
    stripped_s = s.strip()
    if len(stripped_s) < 1:
        return False
    if len(stripped_s) == 1:
        if stripped_s in char_in_integer_string[2:]:
            return True
    if len(stripped_s) > 1:
        if stripped_s[0] in char_in_integer_string and\
            stripped_s[1:] in char_in_integer_string[2:]:
            return True    
    return False

# Read a string from user and display if it represnts an integer
def main():
    s = input("Please, enter a string: ")
    if isInteger(s):
        print("%s is an integer string" % s)
    else:
        print("%s is not an integer string" % s)

# Call the main function:
if __name__ == "__main__":
    main()
    
    
    
