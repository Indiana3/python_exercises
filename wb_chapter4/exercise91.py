##
# Convert a gregorian date to an ordinal date 
#

## Convert a gregorian date to an ordinal date
# @param d the day in a month from 1 to 31
# @param m the month in the year from 1 to 12
# @param y the current year
# @return the day in the year from 1 to 365 or 366
#

def ordinalDate(d, m, y):
    # Store the number of days in each month (except February and December)
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
    
    # Determine is year is leap
    if y % 4 == 0:
        days_in_february = 29
    else:
        days_in_february = 28
    
    # Count the days in the previous months
    if m >= 1:
        days_in_previous_months = 0
    if m >= 2:
        days_in_previous_months += DAYS_IN_JANUARY
    if m >= 3:
        days_in_previous_months += days_in_february
    if m >= 4:
        days_in_previous_months += DAYS_IN_MARCH
    if m >= 5:
        days_in_previous_months += DAYS_IN_APRIL
    if m >= 6:
        days_in_previous_months += DAYS_IN_MAY
    if m >= 7:
        days_in_previous_months += DAYS_IN_JUNE
    if m >= 8:
        days_in_previous_months += DAYS_IN_JULY
    if m >= 9:
        days_in_previous_months += DAYS_IN_AUGUST
    if m >= 10:
        days_in_previous_months += DAYS_IN_SEPTEMBER
    if m >= 11:
        days_in_previous_months += DAYS_IN_OCTOBER
    if m >= 12:
        days_in_previous_months += DAYS_IN_NOVEMBER
    
    # Compute the corresponding day in the ordinal date
    ordinal_day = days_in_previous_months + d
    return ordinal_day

# Read a gregorian date and display the corresponding
# ordinal date
def main():
    d = int(input("Please, enter a day of a month: "))
    m = int(input("Please, enter a month of the year: "))
    y = int(input("Please, enter a year: "))

    print("The ordinal date is %i %i" % (ordinalDate(d, m, y), y))

# Run the programm
if __name__ == "__main__":
    main()
    
    

    
         
    