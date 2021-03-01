##
# Generate a random password
#
from random import randrange

# Define the following constants:
PW_MIN_LEN = 7
PW_MAX_LEN = 10
ASCII_LOWER_POSITION = 33
ASCII_HIGHER_POSITION = 126

## Generate a random password with a length between 7 and 10
# and characters from 33 to 126 positions of ASCII table
# @return the password
def randomPassword():
    
    # Generate a random len for the password between 7 and 10 characters
    password_len = randrange(PW_MIN_LEN, PW_MAX_LEN + 1)

    # Choose a random character from 33 to 126 positions of ASCII table
    password = ""
    for i in range(password_len):
        password += chr(randrange(ASCII_LOWER_POSITION, ASCII_HIGHER_POSITION + 1))
    return password

# Display the random password generated
def main():
    print(randomPassword())

# Call the main function:
if __name__ == "__main__":
    main()

