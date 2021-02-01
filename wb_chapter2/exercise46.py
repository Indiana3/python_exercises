##
# Determine whether a square of a chessboard is black or white
#

# Read a position from the user
position = input("Please, write a position (e. g. a1): ")
letter = position[0]
number = int(position[1])

# Determine whether a square is black or white
if letter == "a" or letter == "c" or letter == "e" or \
    letter == "g":
    if number % 2 == 0:
        color = "white"
    else:
        color = "black"
else:
    if number % 2 == 0:
        color = "black"
    else:
        color = "white"

# Display the position
print("The position", position, "is a square", color)