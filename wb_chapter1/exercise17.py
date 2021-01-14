##
# Compute the amount of energy required to achieve
# the desired temperature change of a mass of water and its
# cost measured in kilowatt hour
#
HEAT_CAPACITY_WATER = 4.186
J_TO_KWH = 2.77778e-7
COST_PER_KWH = 8.9 

# Read the mass and temperature change from users
print("Please, enter: ")
volume = float(input("the volume of water in milliliters: "))
start_temperature = float(input("the start temperature: "))
final_temperature = float(input("the final temperature: "))

# Compute the amount of energy
delta_t = final_temperature - start_temperature
q = volume * HEAT_CAPACITY_WATER * delta_t

# Convert energy from joule to kilowatt hours
kwh = abs(q * J_TO_KWH)

# Compute the cost of energy in kilowatt hours
total_cost = kwh * COST_PER_KWH

# Display the amount of energy required and its cost
print("The amount of energy required is %i J" % q,
"and its cost is %.2f cents" % total_cost)
