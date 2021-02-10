##
# Converte Celsius degrees multiples of 10
# into Fahrenheit degrees in range 0-100° C
#
 
# Display the headings of the table
print("°Celsius".ljust(15), "==>", "°Fahrenheit".rjust(18) )   
print()

# Display conversion for multiples of
celsius = 0
while celsius <= 100:
    fahr = (celsius * (9/5)) + 32
    print("%4i°C" % celsius, "==>".rjust(12), "%12i°F" % fahr)
    celsius = celsius + 10