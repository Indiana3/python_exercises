##
# Read, tokenize and mark the unary operators
# in a mathematical expression
#
from exercise129 import tokenGenerator

## Identify unary operators "+" and "-" in a list of tokens
# @param t a list of tokens
# @return a new list where unary operators have been replaced
# by "u+" and "u-" respectively
#
def unaryIdentifier(t):
    # Create a new list to store tokens
    mod_tokens = []
    # For each element of the tokens list
    i = 0
    while i < len(t):
        # Check if the element is "+" or "-"
        if t[i] == "+" or t[i] == "-":
            # Check if it's the first element of the list or
            # if preceded by an operator or an open parenthesis
            if i == 0 or t[i-1] == "(" or \
            t[i-1] == "[" or t[i-1] == "{" or \
            t[i-1] == "+" or t[i-1] == "-" or \
            t[i-1] == "*" or t[i-1] == "/" or \
            t[i-1] == "^":
                # Mark the operator with "u" char 
                mod_token = "u" + t[i]
                mod_tokens.append(mod_token)
                i = i+1
                continue
        # If the last conditions are false, add
        # the element without modifications
        mod_tokens.append(t[i])
        i = i+1
    return mod_tokens

# Read a string from user, tokenize it and
# mark the unary operators
def main():
    exp = input("Please enter a valid mathematical expression: ")
    # Display the tokens list
    tokens = tokenGenerator(exp)
    # print(tokens)
    # Display the tokens list with unary operators marked (if any)
    print(unaryIdentifier(tokens))

# Call the main function
if __name__ == "__main__":
    main()
