##
# Compute the regular price of bread, the discount and the
# total price
#
LOAVE_PRICE = 3.49
DISCOUNT_RATE = 0.6

# Read the number of old loaves
loaves = int(input("Please enter the number of old loaves: "))

# Compute the regular price, the discount and the total price
reg_price = loaves * LOAVE_PRICE
discount = reg_price * DISCOUNT_RATE
tot_price = reg_price - discount

# Display the results
print("Regular price:       %6.2f" % reg_price)
print("Discount:            %6.2f" % discount)
print("Total:               %6.2f" % tot_price)

