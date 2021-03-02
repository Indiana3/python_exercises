##
# Generate a random license plate 
#
from random import randint

## Generate a random license plate 
# @return a string of characters made of 3 letters followed by 3 digits or
# 4 digits followed by 3 letters with equal odds
def randomLicensePlate():
    # Store ASCII character positions as constants
    ASCII_LETTER_A_UPPER = 65
    ASCII_LETTER_Z_UPPER = 90
    ASCII_DIGIT_0 = 48
    ASCII_DIGIT_9 = 57
    
    # Set license_plate equal to an empty string
    license_plate = ""
    
    # Determine with equal odds which license plate format
    # will be generated
    license_format = randint(0, 1)
    
    # if 0 is sorted, then license plate will have 3 letters followed by 3 digits
    if license_format == 0:
        for _ in range(3):
            license_plate += chr(randint(ASCII_LETTER_A_UPPER, ASCII_LETTER_Z_UPPER)) 
        for _ in range(3):
            license_plate += chr(randint(ASCII_DIGIT_0, ASCII_DIGIT_9)) 
    
    # if 1 is sorted, then license plate will have 4 digits followed by 3 letters
    elif license_format == 1:
        for _ in range(4):
            license_plate += chr(randint(ASCII_DIGIT_0, ASCII_DIGIT_9))
        for _ in range(3):
            license_plate += chr(randint(ASCII_LETTER_A_UPPER, ASCII_LETTER_Z_UPPER))
    
    return license_plate

# Display the random license plate generated
def main():
    print("The random license plate genereted is {}".format(randomLicensePlate()))

# Call the main function
main()


