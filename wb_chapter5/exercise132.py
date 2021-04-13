##
# Evaluete a postfix expression
#
from exercise96 import isInteger
from exercise97 import operatorPrecedence
from exercise129 import tokenGenerator
from exercise130 import unaryIdentifier
from exercise131 import infixToPostfix

## Evaluate a postfix expression
# @param postfix a tokens list representing in postfix form
# @return evaluation of the postfix expression
#
def evaluatePostfix(postfix):
    # Create an empty list to store values
    values = []
    # For each token in the postfix expression
    for i in range(len(postfix)):
        # The token is a number
        if isInteger(postfix[i]):
            values.append(int(postfix[i]))
        # The token is an unary minus
        elif postfix[i] == "u-":
            value = values.pop()
            values.append(-value)
        # The token is a binary operator
        elif postfix[i] in ["+", "-", "*", "/", "**"]:
            right = str(values.pop())
            left = str(values.pop())
            result = left + postfix[i] + right
            values.append(eval(result))
    return values[0]

# Read a valid mathematical expression from user,
# convert it to a tokens list,
# convert from infix to postfix form
# evaluate and print the expression
def main():
    exp = input("Please, enter a valid mathematical expression: ")
    tokens = tokenGenerator(exp)
    tokens_with_unary = unaryIdentifier(tokens)
    postfix = infixToPostfix(tokens_with_unary)
    print(evaluatePostfix(postfix))

# Call main function
if __name__ == "__main__":
    main()

