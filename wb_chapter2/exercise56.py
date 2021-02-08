##
# Determine the name of the radiation corresponding to
# the entered frequency
#
MICROWAVES_LOW_EXTREME = 3.0e9
INFRARED_LIGHT_LOW_EXTREME = 3.0e12
VISIBLE_LIGHT_LOW_EXTREME = 4.3e14
ULTRAVIOLET_LIGHT_LOW_EXTREME = 7.5e14
X_RAYS_LOW_EXTREME = 3.0e17
GAMMA_RAYS_LOW_EXTREME = 3.0e19

# Read the frequency in hz from the user
frequency = float(input("Please, enter a frequency in hz" \
" using scientific notion (e.g. 3.0e9): "))

# Determine the name of radiation
if frequency < MICROWAVES_LOW_EXTREME:
    radiation = "radio waves"
elif frequency >= MICROWAVES_LOW_EXTREME and \
    frequency < INFRARED_LIGHT_LOW_EXTREME:
    radiation = "micro waves"
elif frequency >= INFRARED_LIGHT_LOW_EXTREME and \
    frequency < VISIBLE_LIGHT_LOW_EXTREME:
    radiation = "infrared light"
elif frequency >= VISIBLE_LIGHT_LOW_EXTREME and \
    frequency < ULTRAVIOLET_LIGHT_LOW_EXTREME:
    radiation = "visible light"
elif frequency >= ULTRAVIOLET_LIGHT_LOW_EXTREME and \
    frequency < X_RAYS_LOW_EXTREME:
    radiation = "ultraviolet light"
elif frequency >= X_RAYS_LOW_EXTREME and \
    frequency < GAMMA_RAYS_LOW_EXTREME:
    radiation = "X-rays"
elif frequency >= GAMMA_RAYS_LOW_EXTREME:
    radiation = "gamma rays"

# Display the result
print(frequency, "corresponds to", radiation)
