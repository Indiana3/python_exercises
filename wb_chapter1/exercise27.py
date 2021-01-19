##
# Compute the month and day for Easter implementing the
# Anonymous Gregorian Computus algorithm
#

# Read the year from the user
year = int(input("Please, enter the current year: "))

# Compute the month and day for Easter
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451
month = (h + l - 7 * m + 114) // 31
day = 1 + (h + l - 7 * m + 114) % 31

# Display the result
print("In the", year, "Easter will be on the %02i-%02i-%i" % (month, day, year))