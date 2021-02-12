##
# Convert a sequence of letter grades into grade points
# and compute its avarage
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

# Initialize to 0 the sum of grade points
# Initialize to 0 the number of letter grades entered
total_points = 0
grades_entered = 0

# Read the first letter grade from the user
letter_grade = input ("Please, enter a letter grade: ")

# Convert into grade points
while letter_grade != "":
    # Convert lowercase chars (if any) in uppercase chars
    letter_grade = letter_grade.upper()
    if letter_grade == "A+" or letter_grade == "A":
        points = A
    elif letter_grade == "A-":
        points = A_MINUS
    elif letter_grade == "B+":
        points = B_PLUS
    elif letter_grade == "B":
        points = B
    elif letter_grade == "B-":
        points = B_MINUS
    elif letter_grade == "C+":
        points = C_PLUS
    elif letter_grade == "C":
        points = C
    elif letter_grade == "C-":
        points = C_MINUS
    elif letter_grade == "D+":
        points = D_PLUS
    elif letter_grade == "D":
        points = D
    elif letter_grade == "F":
        points = F
    # Sum the converted points to the previous points
    total_points = total_points + points
    # Increment of 1 the number of letter grades entered
    grades_entered = grades_entered + 1
    letter_grade = input ("Please, enter the next letter grade: ")   
    
# Compute the avarage of grade points
points_avarage = total_points / grades_entered

# Display the result
print("The avarage of grade points is %.2f" % points_avarage)