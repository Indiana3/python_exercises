##
# Determine and display whether an integer number is even or odd
#

# Read an integer number
num = int(input("Please, enter an integer number: "))

# Determine whether num is even or odd and display the result
if num % 2 == 0:
    print(num, "is an even integer number")
else:
    print(num, "is an odd integer number")
