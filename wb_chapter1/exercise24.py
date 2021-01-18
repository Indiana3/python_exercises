##
# Converts units of time in seconds
#
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

# Read a duration of time as a number of days, hours, minutes and seconds
print("Please, enter: ")
d = int(input("the number of days: "))
h = int(input("the number of hours: "))
m = int(input("the number of minutes: "))
s = int(input("the number of seconds: "))

# Convert all the units of time in seconds and sum the values
tot_s = ((d * HOURS_PER_DAY + h) * MINUTES_PER_HOUR + m) * SECONDS_PER_MINUTE + s

# Display the result
print(d, "days,", h, "hours,", m, "minutes,", s, "seconds are equal to")
print(tot_s, "seconds")

