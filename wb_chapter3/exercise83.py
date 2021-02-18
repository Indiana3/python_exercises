##
# Determine the maximum integers in a collection of numbers
# randomly selected from 1 to 100
#
from random import randint

# Generate and print the first random integer  
# Initialize the maximum value found with first number
# Initialize to 0 the times the new genereted number is greater than the previous one
first_num = randint(1, 101)
print(first_num)
max_value = first_num
greater = 0

# For each number randomly genereted, check if it is
# greater then the maximum found so far
for i in range(1, 100):
    num = randint(1, 100)
    if num > max_value:
        print(num, "<=== Update")
        max_value = num
        greater = greater + 1
    else:
        print(num)

# Display the max value found and the number of updates
print("The maximum value found was %i" % max_value)
print("The maximum value was updated %i times" % greater)