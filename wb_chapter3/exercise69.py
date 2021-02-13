##
# Compute the total cost of zoo adimission for
# a group of guests
#

# Store the admissions prices as constants
LITTLE_CHILD_PRICE = 0.00
CHILD_PRICE = 14.00
SENIOR_PRICE = 18.00
ADULT_PRICE = 23.00

# Store the age limits as constants
LITTLE_CHILD_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

# Inizialize to 0 the total price paid by the group of guests
total_price = 0

# Keep asking guest age until he/she enters a blank line
age = input("Please, enter your age (blank line to finish): ")

# Add the correct price to the total price
while age != "":
    age = int(age)
    if age <= LITTLE_CHILD_LIMIT:
        total_price = total_price + LITTLE_CHILD_PRICE
    elif age <= CHILD_LIMIT:
        total_price = total_price + CHILD_PRICE
    elif age <= ADULT_LIMIT:
        total_price = total_price + ADULT_PRICE
    else:
        total_price = total_price + SENIOR_PRICE

    # Ask for the age of the next guest
    age = input("Please, enter your age (blank line to finish): ")

# Display the total price paid by the group
print("The total price you pay is $%.2f" % total_price)
