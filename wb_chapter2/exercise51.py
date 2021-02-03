##
# Display the number and the values (if any) 
# of the real roots of a quadratic function
#
from math import sqrt

# Read the constants a, b, c from user
a = float(input("Please, enter the value of a: "))
b = float(input("Please, enter the value of b: "))
c = float(input("Please, enter the value of c: "))

# Compute and display the number and the values (if any) of real roots
if b ** 2 - 4 * a * c < 0:
    roots_num = 0
    print("This quadratic equation has", roots_num, "roots")
elif b ** 2 - 4 * a * c == 0:
    roots_num = 1
    root = -b / (2 * a)
    print("This quadratic equation has", roots_num, "root and its value is", root)
elif b ** 2 - 4 * a * c > 0:
    roots_num = 2
    root_1 = -b + sqrt(b ** 2 - 4 * a * c) / (2 * a)
    root_2 = -b - sqrt(b ** 2 - 4 * a * c) / (2 * a)
    print("This quadratic equation has", roots_num, "roots and its values are %f and %f" % (root_1, root_2))




