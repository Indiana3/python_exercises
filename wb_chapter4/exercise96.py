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
    for i in range(0, len(stripped_s)):
        if i == 0:
            if stripped_s[i] in char_in_integer_string:
                pass
            else:
                return False
        else:
            if stripped_s[i] in char_in_integer_string[2:]:
                pass
            else:
                return False
        i = i + 1
    return True

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
    
    
    
