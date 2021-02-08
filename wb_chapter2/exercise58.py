##
# Says whether the year entered is leap
#

# Read the year from the user:
year = int(input("Please, enter a year: "))

# Determine whether the year is leap
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

# Display the result
if is_leap:
    print(year, "is leap")
else:
    print(year, "is not leap")