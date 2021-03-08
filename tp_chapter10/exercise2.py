## Create a new list where the ith element is the sum of the ith + 1 elements
# @param t a list of integers
# @return the cumulative sum
def cumsum(t):
    t1 = []
    total = 0
    for i in range (0, len(t)):
        total += t[i]
        t1.append(total)
    return t1

# Call the cumsum function and display the result
print(cumsum([10, 5, 3]))