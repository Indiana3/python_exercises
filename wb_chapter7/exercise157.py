##
# Convert grade points to letter grade and viceversa
#

# Create a dictionary with letter grades as keys
# and grade points as values
letter_points = {
    "A+" : 4.1,
    "A" : 4.0,
    "A-" : 3.7,
    "B+" : 3.3,
    "B" : 3.0,
    "B-" : 2.7,
    "C+" : 2.3,
    "C" : 2.0,
    "C-" : 1.7,
    "D+" : 1.3,
    "D" : 1.0,
    "F" : 0.0
}

# Read the first grade from the user
grade = input("Please, enter a grade point or letter grade: ")

# Until the user doesn't enter a blank line
while grade != "":
    try:
        # If the grade is a float value, convert it
        # to its corrisponding letter grade
        grade = float(grade)
        if grade > 4.0:
            print("A+")
        elif grade >= 3.8 and grade <= 4.0:
            print("A")
        elif grade >= 3.5 and grade < 3.8:
            print("A-")
        elif grade >= 3.2 and grade < 3.5:
            print("B+")
        elif grade >= 2.9 and grade < 3.2:
            print("B")
        elif grade >= 2.5 and grade < 2.9:
            print("B-")
        elif grade >= 2.2 and grade < 2.5:
            print("C+")
        elif grade >= 1.9 and grade < 2.2:
            print("C")
        elif grade >= 1.5 and grade < 1.9:
            print("C-")
        elif grade >= 1.2 and grade < 1.5:
            print("D+")
        elif grade >= 0.5 and grade < 1.2:
            print("D")
        elif grade >= 0.0 and grade < 0.5:
            print("F")
        # Display an error message if the float number is negative
        else:
            print("There's no negative scores")

    except:
        # If the grade is a letter, convert it
        # to its corresponding grade points
        try:
            grade = grade.upper()
            print(letter_points[grade])
        
        except:
            # Display an error message if the letter isn't in the dictionary
            print("The supplied input is invalid")
    
    # Ask to the following grade
    grade = input("Please, enter another grade point or letter grade: ")
