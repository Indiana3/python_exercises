## Calculate the shipping charge for n items in the order
# @param items number of items ordered
#
def shipping_charge(items):
    CHARGE_FOR_FIRST_ITEM = 10.95
    CHARGE_FOR_NEXT_ITEM = 2.95
    if items == 0:
        return 0
    else:
        total_charge = CHARGE_FOR_FIRST_ITEM + \
            CHARGE_FOR_NEXT_ITEM * (items - 1)
        return total_charge

# Read the number of items ordered by the user
items = int(input("How many items do you want to buy? "))

# Calculate and display the shipping charge
print("You ordered %i items. You pay $%.2f for shipping charge" \
    % (items, shipping_charge(items)))