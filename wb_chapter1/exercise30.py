##
# Celsius converted in Fahrenheit and Kelvin degrees
#

# Read the temperature in Celsius
celsius = float(input("Enter a temperature in Celsius degrees: "))

# Convert Celsius to Fahrenheit degrees
fahr = (9/5 * celsius) + 32

# Convert Celsius to Kelvin degrees
k = celsius + 273.15

# Display the results
print(celsius, "°C are equal to: ")
print(fahr, "°F")
print(k, "K")