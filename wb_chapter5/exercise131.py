## Convert a list of tokens representing an infix expression
# to the equivalent postfix expression
#
from exercise96 import isInteger
from exercise97 import operatorPrecedence
from exercise129 import tokenGenerator
from exercise130 import unaryIdentifier

## Convert a list of tokens representing an infix expression
# to a postfix expression
# @param tokens_with_unary a list of tokens with unary operators marked
# return a list of tokens representing the equivalent postfix expression
#
def infixToPostfix(tokens_with_unary):
    # Create an empty list to store operators
    operators = []
    # Create an empty list to store postfix
    postfix = []
    # Check each token of the list
    for i in range(len(tokens_with_unary)):
        # Token is an integer
        if isInteger(tokens_with_unary[i]):
            postfix.append(tokens_with_unary[i])
        else:
            # Token is an operator
            if tokens_with_unary[i] in ["+", "-", "u+", "u-",
            "*", "/", "**"]:
                while len(operators) != 0 and operators[-1] not in \
                    ["(", "[", "{"] and operatorPrecedence(tokens_with_unary[i]) \
                        < operatorPrecedence(operators[-1]):
                        operator = operators.pop()
                        postfix.append(operator)
                operators.append(tokens_with_unary[i])
            # Token is an open parenthesis
            if tokens_with_unary[i] in ["(", "[", "{"]:
                operators.append(tokens_with_unary[i])
            # Token is a close parenthesis
            if tokens_with_unary[i] in [")", "]", "}"]:
                while operators[-1] not in ["(", "[", "{"]:
                    operator = operators.pop()
                    postfix.append(operator)
                # Remove the open parenthesis from operators
                operators.pop()
    # Each left item of operators must be appended to postfix
    while len(operators) != 0:
        operator = operators.pop()
        postfix.append(operator)
    
    return postfix

# Read a valid string from user and print the
# corresponding list of tokens in postfix form
def main():
    exp = input("Please, enter a valid mathematical expression: ")
    # Generate the list of tokens in infix form
    tokens = tokenGenerator(exp)
    # Mark the unary operators in the list
    tokens_with_unary = unaryIdentifier(tokens)
    # Print the list of tokens in postfix form
    print(infixToPostfix(tokens_with_unary))

# Call main function
if __name__ == "__main__":
    main()

    



