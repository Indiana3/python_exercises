##
# Read integers from user and display each value in ascending order
# 

# Start with an empty list
integers = []

# Read integers and store them in integers until the user type 0
num = int(input("Please, enter an integer (enter 0 to stop): "))
while num != 0:
    integers.append(num)
    num = int(input("Please, enter another integer (enter 0 to stop): "))

# Sort all the values in ascending order using sort method
# integers.sort()

# Sort all the values in ascending order ussing sorted function
sorted_integers = sorted(integers)

# Print each of them in a different line
print("The integers in ascending order are: ")
for integer in sorted_integers:
    print(integer)