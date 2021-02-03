##
# Determine the intensity of an earthquake from magnitude in Richter Scale
#

# Read the magnitude from the user
mag = float(input("Please, enter the magnitude according to Richter Scale: "))

# Determine the intensity of the earthquake
if mag < 2.0:
    intensity = "micro"
elif mag >= 2.0 and mag < 3.0:
    intensity = "very minor"
elif mag >= 3.0 and mag < 4.0:
    intensity = "minor"
elif mag >= 4.0 and mag < 5.0:
    intensity = "light"
elif mag >= 5.0 and mag < 6.0:
    intensity = "moderate"
elif mag >= 6.0 and mag < 7.0:
    intensity = "strong"
elif mag >= 7.0 and mag < 8.0:
    intensity = "major"
elif mag >= 8.0 and mag < 10.0:
    intensity = "great"
elif mag >= 10.0:
    intensity = "meteoric"

# Display the result
print("An earthquake with magnitude of", mag, "is considered", intensity )