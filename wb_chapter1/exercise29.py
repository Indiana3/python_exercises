## 
# Compute the wind chill index
#

# Read the air temperature and wind speed
print("Please, enter: ")
t = float(input("the air temperature less or equal" \
" to 10° C: "))
v = float(input("the wind speed exceeding 4.8 km/h: "))

# Compute the wind chill index
wci = 13.12 + 0.6215 * t - 11.37 * v ** 0.16 + 0.3965 * t * v ** 0.16

# Display the wind chill index
print("The wind chill index is", round(wci))