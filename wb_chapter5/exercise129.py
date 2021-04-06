##
# Read a string containing a valid mathematical expression
# and display its substrings of tokens
#

## Break a string containing a mathematical expression
# into a list of tokens
# @param s a string
# @return a list of tokens
#
def tokenGenerator(s):
    # Delete all whitespaces from the string (if any)
    s = s.split()
    # Join all characters of the string in a string
    # without whitespaces
    s = "".join(s)
    ## Create a list for each category of available characters
    # All digits are available
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # All parentheses are available
    parentheses = ["(", ")", "[", "]", "{", "}"]
    # Operators available
    operators = ["+", "-", "*", "/", "^"]
    # Create a tokens list to store tokens
    tokens = []
    # For each char of s
    i = 0
    while i < len(s):
        # If the char is a parenthesis or an operator,
        # add it directly to tokens
        if s[i] in parentheses or s[i] in operators:
            tokens.append(s[i])
            i = i+1
        # If the char is a digit, check if there are consecutive digits
        # before adding it/them to tokens
        elif s[i] in digits:
            # Create num variable as an empty string
            num = ""
            while i < len(s) and s[i] in digits:
                num = num + s[i]
                i = i+1
            # Add num to tokens
            tokens.append(num)
        # If the char is something else, return an empty list
        else:
            return []
    return tokens

# Create a function including the main program
def main():
    # Read a valid string from user
    s = input("Please, enter a string containing a valid mathematical expression: ")
    # Display the list of tokens
    print("From %s have been generated the following tokens: " %(s))
    print(tokenGenerator(s))

# Call the main function
if __name__ == "__main__":
    main()