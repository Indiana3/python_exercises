##
# Display the frequency of a note C0 to C8
#
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

# Read the note and the octave from the user
name = input("Please, enter the two characters note name (e.g. C4): ")

# Store the note and the octave in separable variables
note = name[0]
octave = int(name[1])

# Get the frequency of the note in Hz, assuming it is in the fourth octave
if note == "C":
    freq = C4_FREQ
elif note == "D":
    freq = D4_FREQ
elif note == "E":
    freq = E4_FREQ
elif note == "F":
    freq = F4_FREQ
elif note == "G":
    freq = G4_FREQ
elif note == "A":
    freq = A4_FREQ
elif note == "B":
    freq = B4_FREQ

# Adjust the frequency according to the octave
freq = freq / 2 ** (4 - octave)

# Display the result
print("The frequency of", name, "is %.2f Hz" % freq)