##
# Convert human years to dog years
#
UP_TO_2 = 10.5
OVER_2 = 4

# Read human age expessed by a positive integer number
human = int(input("Please, enter human years: "))

# Conversion from human years to dog years
if human < 0:
    print("Please, enter a positive number")
elif human == 1:
    print(human, "human years are %.1f" % UP_TO_2, "dog years")
elif human == 2:
    dog = human * UP_TO_2
    print(human, "human years are %i" % dog, "dog years")
else:
    dog = 2 * UP_TO_2 + (human - 2) * OVER_2
    print(human, "human years are %i" % dog, "dog years")
