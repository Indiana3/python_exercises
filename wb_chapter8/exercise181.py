## Check if the value in dollars can be reached 
# using a defined number of coins
# @param dollars a float representing a value in dollars
# @param coins an integer representing the number of coins
# @return True if the value can be reached using the defined
# number of coins; False otherwise
#
def possibleChange(dollars, coins, dollars_subtracted = 0):
    # Coins values
    coins_values = [0.01, 0.05, 0.10, 0.25]
    # Remember the original values of dollars and coins
    # Base cases
    # No money and no coins return True
    if dollars == 0 and coins == 0:
        return True
    # Either no money and coins or
    # money and no coins return False
    # Try with the following value in the list
    if dollars == 0 or coins == 0:
        coins_values.pop(0)
        dollars = dollars + dollars_subtracted
        dollars_subtracted = 0
        if len(coins_values) == 0:
            return False
    # Recursive cases
    # Try with the first element in the list
    coin_value = coins_values[0]
    # Store the money you subtract in a variable
    dollars_subtracted += coin_value
    return possibleChange(dollars-coin_value, coins-1)


print(possibleChange(0.50, 2))


        
    