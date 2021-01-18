##
# Convert time duration from seconds to a corresponding value of
# days, hours, minutes and seconds
#
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOURS = 60
HOURS_PER_DAY = 24

# Read a number of seconds
tot_s = int(input("Please, enter a number of seconds: "))

# Compute the corresponding value in days, hours, minutes and seconds
s = tot_s % SECONDS_PER_MINUTE
tot_m = tot_s / SECONDS_PER_MINUTE 
m = tot_m % MINUTES_PER_HOURS
tot_h = tot_m / MINUTES_PER_HOURS
h = tot_h % HOURS_PER_DAY
d = tot_h / HOURS_PER_DAY

# Display the result
print(tot_s, "seconds correspond to: ")
print("%02i days" % d)
print("%02i hours" % h)
print("%02i minutes" % m)
print("%02i seconds" % s)