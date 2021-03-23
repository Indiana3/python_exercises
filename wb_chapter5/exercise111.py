##
# Read integers, store them in a list and display them in reverse order
#

# Start with an empty list
integers = []

# Read integers from user and add them to the list until he types 0
num = int(input("Please, enter an integer (0 to stop): "))
while num != 0:
    integers.append(num)
    num = int(input("Please, enter another integer (0 to stop): "))

# Arrenge list elements in reverse order
integers.reverse()

# Display each integer in a line
print("The integers in reverse order are: ")
for integer in integers:
    print(integer)