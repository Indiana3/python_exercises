##
# Say how the performance of an employee is acceptable and his raise
#
RATING_UNACCEPTABLE = 0.0
RATING_ACCEPTABLE = 0.4
RATING_MERITORIOUS = 0.6
SALARY = 2400

# Read a rating from the user
rating = float(input("Please, enter the employee's rating: "))

# Determine how good the employee's performance is 
if RATING_UNACCEPTABLE < rating < RATING_ACCEPTABLE or \
    RATING_ACCEPTABLE < rating < RATING_MERITORIOUS:
    print("You have entered an invalid rating")
    quit()
elif rating == RATING_UNACCEPTABLE:
    performance = "unacceptable"
elif rating == RATING_ACCEPTABLE:
    performance = "acceptable"
elif rating >= RATING_MERITORIOUS:
    performance = "meritorious"

# Determine the employee's salary increase
salary_increase = SALARY * rating

# Display the result
print(rating, "rating corresponds to a/an", performance, "performance")
print("The salary increases of $", salary_increase)

 