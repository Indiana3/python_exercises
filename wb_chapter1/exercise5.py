## 
# Compute the refund for returning containers
#
ONE_LITER_DEPOSIT = 0.10
MORE_LITERS_DEPOSIT = 0.25

# Take the containers number from users
one_liter_number = int(input("Enter the number of your 1 liter containers: "))
more_liters_number = int(input("Enter the number of your over 1 liter containers: "))

# Compute the total refund
refund = one_liter_number * ONE_LITER_DEPOSIT + more_liters_number * MORE_LITERS_DEPOSIT

# Display the output
print("Your refund is $%.2f" % refund)