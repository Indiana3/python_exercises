##
# Display the total cost of n products, rounded to the
# nearest nickel if customer pays with cash
#
PENNIES_PER_NICKEL = 5
NICKEL = 0.05

# Read first price from user
price = input("Please, enter the first price (blank if you do not have any products): ")

# For each product, determine its price 
total_price_card = 0
total_price_cash = 0

while price != "":
    # if pay with cards
    price = float(price)
    total_price_card += price

    # if pay with cash
    pennies = price * 100
    remainder = pennies % PENNIES_PER_NICKEL
    if remainder == 0:
        price = price
    else:
        if remainder < 2.5:
            price = price - remainder / 100
        else:
            price = price + NICKEL - remainder / 100
    total_price_cash += price

    # Enter the next price
    price = input("Please, enter the next price (blank if you do not have any products): ")

# Display the result
# If you pay with cards
print("You pay $%.2f" % total_price_card, "if you pay with cards")

# If you pay with cash
print("You pay $%.2f" % total_price_cash, "if you pay with cash")