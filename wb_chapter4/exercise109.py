##
# Find and print the magic dates in 20th century
#
from exercise106 import daysInMonth

## Find a magic date (if day times month is equal at the last 2 digits of year)
# @param day a day
# @param month a month
# @param year a year
# return True if a date is magic; False otherwise
def isMagicDate(day, month, year):
    year = int(str(year)[2:])
    if day * month == year:
        return True
    return False

# Print all the magic date in 20th century
def main():
    for y in range (1900, 2000):
        for m in range(1, 13):
            days = daysInMonth(m, y)
            for d in range (1, days + 1):
                if isMagicDate(d, m, y) == True:
                    print("%i/%i/%i" % (d, m, y))

# Call the main function
main()
