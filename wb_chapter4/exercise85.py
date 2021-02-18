## Compute the hypothenuse of a right triangle
# @param side_1 the length of first side
# @param side_2 the length of secondo side
def hypotenuse(side_1, side_2):
    from math import sqrt
    hypotenuse = sqrt(side_1 ** 2 + side_2 ** 2)
    return hypotenuse

# Read the length of the 2 shorter sides from user
side_1 = float(input("Please, enter the length of the first side: "))
side_2 = float(input("Please, enter the length of the first side: "))

# Compute and display the hypotenuse calling hypotenuse()
print("The length of hypotenuse is %.2f" % hypotenuse(side_1, side_2))



