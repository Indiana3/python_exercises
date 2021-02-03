##
# Display your animal sign according to Chinese Zodiac
#

# Read the birth year from the user
year = int(input("Please, enter your birth year: "))

# Determine the animal associated with the year
if year < 0:
    print("You have to enter a year greater or equal to 0")
    quit()
else:
    if year % 12 == 8:
        sign = "Dragon"
    elif year % 12 == 9:
        sign = "Snake"
    elif year % 12 == 10:
        sign = "Horse"
    elif year % 12 == 11:
        sign = "Sheep"
    elif year % 12 == 0:
        sign = "Monkey"
    elif year % 12 == 1:
        sign = "Rooster"
    elif year % 12 == 2:
        sign = "Dog"
    elif year % 12 == 3:
        sign = "Pig"
    elif year % 12 == 4:
        sign = "Rat"
    elif year % 12 == 5:
        sign = "Ox"
    elif year % 12 == 6:
        sign = "Tiger"
    elif year % 12 == 7:
        sign = "Hare"

# Display the result
print("Year", year, "is in the sign of", sign)