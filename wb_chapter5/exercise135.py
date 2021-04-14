##
# Compute all the prime numbers before 2 and some limits
#

# Take a limit from user
limit = int(input("Please, enter a limit (integer number): "))
# Create an empty list to store values
nums = []
# Create a list of integers from 0 to LIMIT
for i in range(limit):
    nums.append(i)
# Cross out 0 and 1 because they aren't prime
del nums[0:2]
# Set p equal to each number of the list not equal to 0
for i in range(len(nums)):
    if nums[i] == 0:
        continue
    p = nums[i]

    # For each number, check if it's a multiple of p
    # If it's a multiple but not equal to p, change
    # it's value with 0
    for j in range(len(nums)):
        if nums[j] == p:
            pass
        else:
            if nums[j] % p == 0:
                nums[j] = 0
# Print all the prime numbers lower than LIMITS
for i in range(len(nums)):
    if nums[i] != 0:
        print(nums[i])














