##
# Convert fuel efficiency from American units into Canadian units
#
K = 235.215

# Read the value from the users
american_units = float(input("Enter the value in American units: "))

# Convert mpg into L/100 Km
canadian_units = K/american_units

# Display the output
print("%.2f MPG are equivalent of %.2f L/100 km" %(american_units, canadian_units))