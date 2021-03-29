##
# Read a collection of points and display the formula
# for the line of best fit in the form y = mx + b
#

# Read a collection of points until x coordinate
# is a blank line
x_coordinates = []
y_coordinates = []
points = 0
x_coordinate = input("Please, enter a value for x (blank to quit): ")
while x_coordinate != "":
    points += 1
    y_coordinate = input("Please, enter a value for y: ")
    x_coordinates.append(float(x_coordinate))
    y_coordinates.append(float(y_coordinate))
    x_coordinate = input("Please, enter a value for x (blank to quit): ")

# Compute m coefficient
# First member: sum of xy products
first_member = 0
for i in range (len(x_coordinates)):
    first_member += x_coordinates[i] * y_coordinates[i]

# Second member: sum of x by sum of y divided by points number
x_sum = 0
for i in range (len(x_coordinates)):
    x_sum += x_coordinates[i]
y_sum = 0
for i in range (len(y_coordinates)):
    y_sum += y_coordinates[i]
second_member = x_sum * y_sum / points

# Third member: sum of squares of x
third_member = 0
for i in range (len(x_coordinates)):
    third_member += x_coordinates[i] ** 2

# Fourth member: squaring of the sum of x divided by points number
fourth_member = x_sum ** 2 / points

# Compute m using all the members of the equation
m = (first_member - second_member) / (third_member - fourth_member)

# Compute b coefficient
avarage_of_x = x_sum / points
avarage_of_y = y_sum / points
b = avarage_of_y - m * avarage_of_x

# Display the formula for the line of best fit
print("The formula for the line of best fit is y = {:.2f}x + {:.2f}".format(m, b))
