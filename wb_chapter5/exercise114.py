## 
# Read a collection of integers, display negative, zeros and positive numbers separatly
# in the same order they were entered
#

# Start with 3 empty list
# 1 for negatives
# 1 for zeros
# 1 for positives
negatives = []
zeros = []
positives = []

# Read an integer from user and add it to the list while a blank line is entered
num = input("Please, enter an integer (blank line to stop): ")
while num != "":
    if int(num) < 0:
        negatives.append(num)
    elif int(num) == 0:
        zeros.append(num)
    elif int(num) > 0:
        positives.append(num)
    num = input("Please, enter another integer (blank line to stop): ")

# Join the 3 lists in a single list so that
# negatives are displayed first, followed by zeros and positives
integers = negatives[:] + zeros[:] + positives[:]

# Display each integer in integers
print("Here the integers you entered: ")
for integer in integers:
    print(integer)