##
# Determine the day of the week for January 1 of a given year
#
from math import floor

SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6

# Read the year from the user
year = int(input("Please, enter a year: "))

# Compute the numeric value of the day for January 1
day_num = (year + floor((year - 1) / 4) - floor((year - 1) / 100)
+ floor((year - 1) / 400)) % 7

# Convert the numeric value into a string value
if day_num == SUNDAY:
    day = "Sunday"
elif day_num == MONDAY:
    day = "Monday"
elif day_num == TUESDAY:
    day = "Tuesday"
elif day_num == WEDNESDAY:
    day = "Wednesday"
elif day_num == THURSDAY:
    day = "Thursday"
elif day_num == FRIDAY:
    day = "Friday"
elif day_num == SATURDAY:
    day = "Saturday"

# Display the result
print("1 January of", year, "is", day)