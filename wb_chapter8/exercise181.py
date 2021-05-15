## Check if the value in dollars can be reached 
# using a defined number of coins
# @param dollars a float representing a value in dollars
# @param coins an integer representing the number of coins
# @return True if the value can be reached using the defined
# number of coins; False otherwise
#
def possibleChange(dollars, coins):
    # Coins values
    PENNY = 0.01
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    # Base cases
    # No money and no coins return True
    if dollars == 0 and coins == 0:
        return True
    # No money and coins left return False
    if dollars <= 0 and coins > 0:
        return False
    # Money and no coins return False
    if dollars > 0 and coins == 0:
        return False
    # Recursive case
    return possibleChange(dollars-PENNY, coins-1) or \
        possibleChange(dollars-NICKEL, coins-1) or \
        possibleChange(dollars-DIME, coins-1) or \
        possibleChange(dollars-QUARTER, coins-1)


print(possibleChange(1, 5))
        
    