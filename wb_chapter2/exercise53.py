##
# Convert grade points into letter grade
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

# Read grade points from the user
points = float(input("Please, enter your grade points: "))

# Convert grade points into letter grade
if abs (points - F) >= abs(A - F):
    letter = "A+"
else:
    if abs(A - points) < abs(A_MINUS - points):
        letter = "A"
    else:
        if abs(A_MINUS - points) < abs(B_PLUS - points):
            letter = "A-"
        else:
            if abs(B_PLUS - points) < abs(B - points):
                letter = "B+"
            else:
                if abs(B - points) < abs(B_MINUS - points):
                    letter = "B"
                else:
                    if abs(B_MINUS - points) < abs(C_PLUS - points):
                        letter = "B-"
                    else:
                        if abs(B_MINUS - points) < abs(C_PLUS - points):
                            letter = "B-"
                        else:
                            if abs(C_PLUS - points) < abs(C - points):
                                letter = "C+"
                            else:
                                if abs(C - points) < abs(C_MINUS - points):
                                    letter = "C"
                                else:
                                    if abs(C_MINUS - points) < abs(D_PLUS - points):
                                        letter = "C-"
                                    else:
                                        if abs(D_PLUS - points) < abs(D - points):
                                            letter = "D+"
                                        else:
                                            if abs(D - points) < abs(F - points):
                                                letter = "D"
                                            else:
                                                letter = "F"

# Display the letter grade
print(points, "grade points are equal to", letter)

