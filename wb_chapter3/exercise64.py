##
# Display original prices, discount amounts and discounted prizes
#
DISCOUNT_RATIO = 0.6
PRICE_INCREASE = 5.00

# Start with the lower prize
prize = 4.95

# For each product shows:
# its original prize
# the discount amount
# the discounted prize
while prize <= 24.95:
    print()
    print("Original prize: %.2f" % prize)
    disc_amount = prize * DISCOUNT_RATIO
    print("Discount amount: %.2f" % disc_amount)
    disc_prize = prize - disc_amount
    print("Discounted prize: %.2f" % disc_prize)
    prize = prize + PRICE_INCREASE
    

