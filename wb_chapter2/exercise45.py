##
# Display if the day and month entered match one of
# the fixed-date holiday
#

# Read the month and the day from the user
print("Please, enter: ")
month = input("the name of a month (like January): ")
day = int(input("a day of the month: "))

# Determine if month and day match a fixed-date holiday
if month == "January" and day == 1:
    print(month, day, "is New Year's Day" )
elif month == "July" and day == 1:
    print(month, day, "is Canada Day" )
elif month == "December" and day == 25:
    print(month, day, "Christmas Day" )
else:
    print("The entered month and day don't correspond to any fixed-date holiday")

