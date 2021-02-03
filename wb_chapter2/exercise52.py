##
# Convert letter grade into grade points
#
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0.0
INVALID = -1

# Read the letter grade from the user
letter = input("Please, enter a letter grade: ")
letter = letter.upper()

# Convert letter into grade points
if letter == "A+" or letter == "A":
    points = A
elif letter == "A-":
    points = A_MINUS
elif letter == "B+":
    points = B_PLUS
elif letter == "B":
    points = B
elif letter == "B-":
    points = B_MINUS
elif letter == "C+":
    points = C_PLUS
elif letter == "C":
    points = C
elif letter == "C-":
    points = C_MINUS
elif letter == "D+":
    points = D_PLUS
elif letter == "D":
    points = D
elif letter == "F":
    points = F
else:
    points = INVALID

# Display the result
if points == INVALID:
    print("You entered an invalid letter grade. Please try again")
else:
    print(letter, "is equivalent to", points, "points")