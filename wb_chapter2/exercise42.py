##
# Display the frequency of a note C0 to C8
#

# Read the note and the octave from the user
note = input("Please, enter the note: ")
octave = int(input("Please, enter the octave: "))

# Compute the corresponding frequency in Hz
if note == "C":
    hz = 261.63
elif note == "D":
    hz = 293.66
elif note == "E":
    hz = 329.63
elif note == "F":
    hz = 349.23
elif note == "G":
    hz = 392.00
elif note == "A":
    hz = 440.00
elif note == "B":
    hz = 493.88

hz = hz / 2 ** (4 - octave)

# Display the result
print("The frequency of", note, octave, "is %.2f" % hz)