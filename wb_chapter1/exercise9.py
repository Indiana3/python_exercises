##
# Compute the savings in the account after 1, 2 and 3 years
#
INTEREST = 0.04

# Read the amount of money deposited from the user
money = float(input("How much money do you want to deposit? "))

# Compute the savings after 1, 2 and 3 years
savings1 = money * INTEREST + money
savings2 = savings1 * INTEREST + savings1
savings3 = savings2 * INTEREST + savings2

# Print the output
print("Your savings after a year are %.2f, " \
    "after 2 years are %.2f, " \
    "after 3 years are %.2f" 
    % (savings1, savings2, savings3))