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
grade_points = float(input("Please, enter your grade points: "))

# Create a grade points list
points = [A, A_MINUS, B_PLUS, B, B_MINUS, C_PLUS, C, C_MINUS, D_PLUS,
D, F]

# Create a letter grade list
letter = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-",
"D+", "D", "F"]

# Convert grade points into letter grade
grade_letter = letter[-1]
i = 0
j = 1
while i < len(points)-1:
    if abs(points[i] - grade_points) < abs(points[i+1] - grade_points):
        grade_letter = letter[j]
        break
    i = i + 1
    j = j + 1
if grade_points >= points[0]:
    grade_letter = letter[0]

# Display the letter grade
print(grade_points, "grade points are equal to", grade_letter)

