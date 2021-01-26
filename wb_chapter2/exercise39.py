##
# Display the number of days in a month
#

# Read the month
month = input("Please, enter the name of a month: ")

# Compute the number of days in a month
days = 31

if month == "april" or month == "june" or month == "september" or month == "november":
    days = 30
elif month == "february":
    days = "28 or 29"

# Display the result
print(month, "has", days, "days in it")
