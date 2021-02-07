##
# Return the color that matches the wavelength
# of visible light spectrum entered by the user
#
VIOLET_WAVELENGTH_STARTS = 380
BLUE_WAVELENGTH_STARTS = 450
GREEN_WAVELENGTH_STARTS = 495
YELLOW_WAVELENGTH_STARTS = 570
ORANGE_WAVELENGTH_STARTS = 590
RED_WAVELENGTH_STARTS = 620
RED_WAVELENGTH_ENDS = 750

# Read the wavelength from the user
wavelength = float(input("Please, enter a wavelength of visible light spectrum in nm: "))

# Determine the corresponding color in spectrum
if wavelength >= VIOLET_WAVELENGTH_STARTS and \
    wavelength < BLUE_WAVELENGTH_STARTS:
    color = "violet"
elif wavelength >= BLUE_WAVELENGTH_STARTS and \
    wavelength < GREEN_WAVELENGTH_STARTS:
    color = "blue"
elif wavelength >= GREEN_WAVELENGTH_STARTS and \
    wavelength < YELLOW_WAVELENGTH_STARTS:
    color = "green"
elif wavelength >= YELLOW_WAVELENGTH_STARTS and \
    wavelength < ORANGE_WAVELENGTH_STARTS:
    color = "yellow"
elif wavelength >= ORANGE_WAVELENGTH_STARTS and \
    wavelength < RED_WAVELENGTH_STARTS:
    color = "orange"
elif wavelength >= RED_WAVELENGTH_STARTS and \
    wavelength <= RED_WAVELENGTH_ENDS:
    color = "red"
else:
    color = ""

# Display the result
if color == "":
    print("This wavelength is not in the visible light spectrum")
else:
    print(wavelength, "nm are", color)

