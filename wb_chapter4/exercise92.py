##
# Read a date from the user and report a second date that
# occurs a pariod of days later
#

from exercise91 import ordinalDate

## Convert ordinal date to gregorian date
# @param d a day within the year
# @param y a year
# @return the corresponding day, month and year
#

def gregorianDate(d, y):
    # Store the number of days for each months (except February and December)
    # as constants
    DAYS_IN_JANUARY = 31
    DAYS_IN_MARCH = 31
    DAYS_IN_APRIL = 30
    DAYS_IN_MAY = 31
    DAYS_IN_JUNE = 30
    DAYS_IN_JULY = 31
    DAYS_IN_AUGUST = 31
    DAYS_IN_SEPTEMBER = 30
    DAYS_IN_OCTOBER = 31
    DAYS_IN_NOVEMBER = 30

    # Determine if year is leap
    if y % 4 == 0:
        days_in_february = 29
        days_in_year = 366
    else:
        days_in_february = 28
        days_in_year = 365
    
    # Check if d is greater than days in a year
    if d > days_in_year:
        while d > days_in_year:
            d = d - days_in_year
            y = y + 1
    
    # Determine the corresponding day for January
    days_in_prev_months = DAYS_IN_JANUARY
    month = 1
    day_of_month = d

    # Determine the corresponding day for the next months
    for i in range (2, 13):
        if d > days_in_prev_months:
            day_of_month = d - days_in_prev_months
            month = i
            if i == 2:
                days_in_prev_months += days_in_february
            if i == 3:
                days_in_prev_months += DAYS_IN_MARCH
            if i == 4:
                days_in_prev_months += DAYS_IN_APRIL
            if i == 5:
                days_in_prev_months += DAYS_IN_MAY
            if i == 6:
                days_in_prev_months += DAYS_IN_JUNE
            if i == 7:
                days_in_prev_months += DAYS_IN_JULY
            if i == 8:
                days_in_prev_months += DAYS_IN_AUGUST
            if i == 9:
                days_in_prev_months += DAYS_IN_SEPTEMBER
            if i == 10:
                days_in_prev_months += DAYS_IN_OCTOBER
            if i == 11:
                days_in_prev_months += DAYS_IN_NOVEMBER
        else:
            break
    return day_of_month, month, y

# Read a gregorian date and a period of days and
# display a second date that occurs after that period of days
def main():
    d = int(input("Please, enter a day: "))
    m = int(input("Please, enter a month: "))
    y = int(input("Please, enter a year: "))
    period = int(input("Please, enter a period of days: "))

    # Convert gregorian date into ordinal date and add period to the result
    new_ordinal_date = ordinalDate(d, m, y) + period

    # Convert the new ordinal date to gregorian date and assign returned tuple
    day_of_month, month, year = gregorianDate(new_ordinal_date, y)

    # Print gregorian date after the period of days
    print("{}/{}/{} after a period of {} days becomes {}/{}/{}".format(d, m, y, period, day_of_month, month, year))

# Run the programm
main()





 
        
            