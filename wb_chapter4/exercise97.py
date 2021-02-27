##
# Determine the precedence of a mathematical operator
#

## Determine which mathematical operator has precedence
# @param s the operator string
# @return an integer representing the precedence of a mathematical operator
#
def precedence(s):
    if s == "+" or s == "-":
        return 1
    if s == "*" or s == "/":
        return 2
    if s == "^":
        return 3
    else:
        return -1

# Read a string representing a mathematical operator from user
def main():
    s = input("Please, enter a mathematical operator: ")
    # Display the precedence according to the integer returned
    # by precedence function
    if precedence(s) == -1:
        print("You didn't enter a mathematical operator")
    else:
        print("The operator {} has precedence {}".format(s, precedence(s)))

# Call the main function
if __name__ == "__main__":
    main()
    
