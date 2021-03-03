##
# Generate a random good password with:
#   at least 8 characters
#   at least 1 uppercase letter
#   at least 1 lowercase letter
#   at least 1 number
#
from exercise100 import randomPassword
from exercise102 import isValidPassword

# Generate a password and display if it meets the requirements
def main():
    password = randomPassword()
    attempts_for_good_password = 1
    while isValidPassword(password) == False:
        password = randomPassword()
        attempts_for_good_password += 1
    print("The valid password {} has been genereted after {} attempts".format(password, attempts_for_good_password))

# Call the main function
main() 