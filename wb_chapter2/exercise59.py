##
# Display the day after the date entered
#

# Read the date from the user
month = int(input("Please, enter the month in numeric form: "))
day = int(input("Please, enter the day in numeric form: "))
year = int(input("Please, enter the year in numeric form: "))

# Determine the day after
if day <= 0 or day > 31:
    day = None
elif month <= 0 or month > 12:
    day = None
elif day > 0 and day < 28:
    day = day + 1
elif day == 28:
    if month == 2:
        if year % 400 == 0 or year % 4 == 0:
            day = 29
        else:
            day = 1
            month = month + 1
    else:
        day = day + 1
elif day == 29:
    if month == 2:
        if year % 400 == 0 or year % 4 == 0:
            day = 1
            month = month + 1
        else:
            day = None
    else:
        day = day + 1
elif day == 30:
    if month == 4 or month == 6 or month == 9 or month == 11:
        day = 1
        month = month + 1
    else:
        day = day + 1
elif day == 31:
    if month == 12:
        day = 1
        month = 1
        year = year + 1
    else:
        day = 1
        month = month + 1

# Display the result
if day == None:
    print("This day doesn't exist")
else:
    print("The next day is %i-%02i-%02i" % (year, month, day))
