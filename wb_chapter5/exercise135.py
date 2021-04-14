##
# Compute all the prime numbers before 2 and some limits
#

# Take a limit from user
limit = int(input("Please, enter a limit (integer number): "))
# Create an empty list to store values
nums = []
# Create a list of integers from 0 to limit
for i in range(limit+1):
    nums.append(i)
# "Cross out" 1 by replacing it with 0
nums[1] = 0
# "Cross out" all multiples of each prime numbers we discover
p = 2
while p < limit:
    # "Cross out" all multiples of p (but not p itself)
    for i in range(p*2, limit+1, p):
        nums[i] = 0
    # Find the next number not "crossed out"
    p = p+1
    while p < limit and nums[p] == 0:
        p = p+1
# Print all the prime numbers lower than limits
print("The prime numbers up to", limit, "are: ")
for num in nums:
    if nums[num] != 0:
        print(num)














