##
# Display three integers from smallest to largest
#

# Read the three numbers
print("Please, enter three integers number: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Compute the smallest, the middle and the largest values
min_value = min(num1, num2, num3)
max_value = max(num1, num2, num3)
mid_value = num1 + num2 + num3 - min_value - max_value

# Display the results
print("The smallest value is", min_value)
print("The middle value is", mid_value)
print("The largest value is", max_value)