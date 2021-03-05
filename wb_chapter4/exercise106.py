##
# Compute the days in a month of the year
#

## Compute the days in a month of year
# @param m a month
# @param y the year
# @return the number of days in that month
def daysInMonth(m, y):
    # For January, March, May, July, August, October and December
    # return 31 days
    if m == 1 or m == 3 or m == 5 or \
        m == 7 or m== 8 or m == 10 or \
            m == 12:
            return 31
    # For February, return 29 days if y is a leap year,
    # 28 days otherwise
    elif m == 2:
        if y % 4 == 0:
            return 29
        else:
            return 28
    # For the other months, return 30 days
    else:
        return 30

# Read the month and the year from the user
# Display the number of days
def main():
    m = int(input("Please, enter a month as an integer between 1 and 12: "))
    y = int(input("Please, enter a year as a four digit integer (e.g. 2021): "))
    d = daysInMonth(m, y)
    print("In the {}° month of {} there are {} days".format(m, y, d))

# Call the main function
main()



          
        

    