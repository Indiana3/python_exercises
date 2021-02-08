##
# Display the total cost of a cell phone plan
#
MINUTES_INCLUDED = 50
MESSAGES_INCLUDED = 50
PLAN_COST = 15
ADDITIONAL_MINUTE_COST = 0.25
ADDITIONAL_MESSAGE_COST = 0.15
CALL_CENTERS_CHARGE = 0.44
SALES_TAX_RATIO = 0.05

# Read the number of minutes and messages from the user
minutes = int(input("Please, enter the number of minutes: "))
messages = int(input("Please, enter the number of messages: "))

# Compute the total cost of minutes
additional_minutes = minutes - MINUTES_INCLUDED
if additional_minutes > 0:
    additional_minutes_cost = ADDITIONAL_MINUTE_COST * additional_minutes
else:
    additional_minutes_cost = 0

# Compute the total cost of messages
additional_messages = messages - MESSAGES_INCLUDED
if additional_messages > 0:
    additional_messages_cost = ADDITIONAL_MESSAGE_COST * additional_messages
else:
    additional_messages_cost = 0

# Compute the entire bill cost without sales tax
bill_cost = PLAN_COST + additional_minutes_cost + additional_messages_cost + \
CALL_CENTERS_CHARGE

# Compute sales tax 
sales_tax = bill_cost * SALES_TAX_RATIO

# Apply sales tax to bill cost
bill_cost = bill_cost + sales_tax

# Display the result
print("Phone plan charge:              $%5.2f" % PLAN_COST)
if additional_minutes_cost != 0:
    print("Additional minutes charge:      $%5.2f" % additional_minutes_cost)
if additional_messages_cost != 0:
    print("Additional messages charge:     $%5.2f" % additional_messages_cost)
print("911 fee:                        $%5.2f" % CALL_CENTERS_CHARGE)
print("Sales tax:                      $%5.2f" % sales_tax)
print("Total bill:                     $%5.2f" % bill_cost)

