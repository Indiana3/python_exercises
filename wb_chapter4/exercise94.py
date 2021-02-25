##
# Determine if three lengths can form a triangle
#

# Check if three lengths form a triangle
# @param a the length 1
# @param b the length 2
# @param c the length 3
# return True if a, b, c are sides of a valid triangle
# return False if they are not

def isATriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a >= b + c or b >= c + a or c >= a + b:
        return False
    return True

# Read three lengths from the user
def main():
    a = float(input("Please, enter the first length: "))
    b = float(input("Please, enter the second length: "))
    c = float(input("Please, enter the third length: "))

    # Display the result calling isATriangle function
    print("{},{},{} can form a triangle? {}".format(a, b, c, isATriangle(a, b, c)))

# Call the main function
main()