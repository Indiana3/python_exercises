##
# Simulate coin flips as long as 3 consecutive occurences
# of the same outcome occur (3 heads or 3 tails)
#
from random import randrange

# Define constants
TOTAL_PERFORMANCES = 10
OUTCOMES = 2
CONSECUTIVES = 3

# Initialize performances with 1
performances = 1
total_flips = 0

# Keep on performing for 10 times
while performances <= TOTAL_PERFORMANCES:
    flips = 0
    head_occurences = 0
    tail_occurences = 0

# Flip the coin until head occurences or tail occurences
# are equal to 3
    while head_occurences < CONSECUTIVES and \
        tail_occurences < CONSECUTIVES:
        if randrange(1, OUTCOMES + 1) == 1:
            print("H", end=" ")
            head_occurences = head_occurences + 1
            tail_occurences = 0
        else:
            print("T", end=" ")
            tail_occurences = tail_occurences + 1
            head_occurences = 0
        flips = flips + 1
    
    # Display the number of flips needed for the current performance
    print("(%i flips)" %flips)
    
    # Add the flips of the current performance to to total flips
    total_flips = total_flips + flips
    performances = performances + 1

# Compute the avarage of flips in 10 performances
flips_avarage = total_flips / TOTAL_PERFORMANCES

# Display the avarage of flips
print("On avarage, %.2f flips were needed" % flips_avarage)

