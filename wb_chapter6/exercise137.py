## 
# Simulate a two dice rolling for n times
#
from random import randint

# Number of times you roll the dice
ROLLING_TIMES = 1000

## Sum the results get on each face
# @param None
# @return the total rolled on 2 dice
#
def rollingDice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    total = dice1 + dice2
    return total

# Store in a dictionary how many times
# you get a total
totals = {}
for i in range(ROLLING_TIMES):
    total = rollingDice()
    if total not in totals:
        totals[total] = 1
    else:
        totals[total] += 1

# For each total, the percent values expected 
expected_percents = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 
6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56,
12: 2.78}

# For each total, display its simulated percent
# along with its expected percent
print("Total    Simulated Percent    Expected Percent")
for total in sorted(totals):
    print("%5i %20.2f %19.2f" % (total, totals[total]/ROLLING_TIMES*100, expected_percents[total]))
    
    

