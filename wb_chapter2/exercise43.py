##
# Convert a frequency to its corresponding note
# Frequencies cover only the notes of the fourth octave
#
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88
LIMIT = 1

# Read a frequency from the user
freq = float(input("Please, enter a frequency in Herz: "))

# Verify whether the frequency corresponds to a note of the
# fourth octave
if C4_FREQ - LIMIT <= freq <= C4_FREQ + LIMIT:
    note = "C4"
elif D4_FREQ - LIMIT <= freq <= D4_FREQ + LIMIT:
    note = "D4"
elif E4_FREQ - LIMIT <= freq <= E4_FREQ + LIMIT:
    note = "E4"
elif F4_FREQ - LIMIT <= freq <= F4_FREQ + LIMIT:
    note = "F4"
elif G4_FREQ - LIMIT <= freq <= G4_FREQ + LIMIT:
    note = "G4"
elif A4_FREQ - LIMIT <= freq <= A4_FREQ + LIMIT:
    note = "A4"
elif B4_FREQ - LIMIT <= freq <= B4_FREQ + LIMIT:
    note = "B4"
else:
    note = ""

# Display the result
if note == "":
    print("The frequency %.2f" % freq, "doesn't correspond " \
          "to a known note")
else:
    print("The frequency %.2f" % freq, "corresponds " \
          "to", note)