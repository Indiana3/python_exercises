##
# Generates 6 numbers from 1 to 49 with no duplicates
# Display them in ascending order
# 
from random import randint

# Each ticket has 6 numbers
NUMBERS_FOR_TICKET = 6

# Numbers drawn are between 1 and 49
FIRST_NUMBER = 1
LAST_NUMBER = 49

# Start with an empty list
ticket_numbers = []

# Generate 6 random numbers between 1 and 49
# Add each number to the list only if it's not already there
while len(ticket_numbers) < NUMBERS_FOR_TICKET:
    num = randint(FIRST_NUMBER, LAST_NUMBER)
    if num not in ticket_numbers:
        ticket_numbers.append(num)

# Sort the numbers in ascending order
ticket_numbers.sort()

# Display the numbers
for number in ticket_numbers:
    print(number)




