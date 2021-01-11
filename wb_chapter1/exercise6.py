##
# Compute the tax, tip and grand total for the meal
#
TAX = 10/100
TIP = 18/100

# Input from the users
meal = float(input("How much cost the meal you ordered? "))

# Compute the tax, tip and grand total
tax = meal * TAX
tip = meal * TIP
grand_total = meal + tax + tip

#Display the output
print("The tax is $%.2f, the tip is $%.2f, " \
      "the grand total is $%.2f" %(tax, tip, grand_total))