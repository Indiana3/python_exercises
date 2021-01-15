##
# Compute the n moles of gas of an ideal gas supplied
# pressure, volume and temperature
#

# Define the ideal gas constant
IDEAL_GAS_CONSTANT = 8.314

# Read the pressure in Pascals, volume in liters and the
# temperature in Celsius or Fahrenheit
print("Please, enter: ")
p = float(input("the pressure in Pascals: "))
v = float(input("the volume in liters: "))
t = input("the temperature in Celsius (C) or Fahrenheit (F): ")

# Convert temperature 
if t[-1] == "C":                 # from Celsius
    t = float(t.strip(" C"))                      
    t = t + 273.15
elif t[-1] == "F":               # from Fahrenheit
    t = float(t.strip(" F"))                                               
    t = (t - 32) * (5/9) + 273.15
else:
    print("Inserisci correttamente la temperatura")
    quit()

# Compute the n moles
n = (p * v) / (IDEAL_GAS_CONSTANT * t)

# Display the result
print("The n moles of gas are %.2f" % n)
