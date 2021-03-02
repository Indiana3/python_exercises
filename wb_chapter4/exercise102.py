##
# Check if the password entered is good or not
#

## Check a password string
# @param s a string
# @return True if s has:
#   at least 8 characters
#   at least 1 uppercase letter (ASCII positions 65-91)
#   at least 1 lowercase letter (ASCII positions 97-123)
#   at least 1 number           (ASCII positions 48-58)
# @return False otherwise
def isValid(s):
    # Check the first condition
    if len(s) < 8:
        return False
    # Check from second to fourth condition
    for i in range(2, 5):
        checked_char = ""
        if i == 2:
            for c in s:
                if c >= "A" and c <= "Z":
                    checked_char = c
                    break
            if checked_char == "":
                return False
        if i == 3:
            for c in s:
                if c >= "a" and c <= "z":
                    checked_char = c
                    break
            if checked_char == "":
                return False
        if i == 4:   
            for c in s:
                if c >= "0" and c <= "9":
                    checked_char = c
                    break
            if checked_char == "":
                return False
    return True

# Read a password from user and check if it's valid
def main():
    s = input("Please, enter a valid password: ")
    print("Valid password? {}".format(isValid(s)))

# Call the main function
if __name__ == "__main__":
    main()
    