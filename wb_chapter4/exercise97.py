##
# Determine the precedence of a mathematical operator
#

## Determine which mathematical operator has precedence
# @param s the operator string
# @return an integer representing the precedence of a mathematical operator
#
def operatorPrecedence(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2
    if operator == "u+" or operator == "u-":
        return 3 
    if operator == "**":
        return 4
    else:
        return -1

# Read a string representing a mathematical operator from user
def main():
    s = input("Please, enter a mathematical operator: ")
    # Display the precedence according to the integer returned
    # by precedence function
    if operatorPrecedence(s) == -1:
        print("You didn't enter a mathematical operator")
    else:
        print("The operator {} has precedence {}".format(s, operatorPrecedence(s)))

# Call the main function
if __name__ == "__main__":
    main()
    
