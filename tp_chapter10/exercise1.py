## Add up the elements from all the nested lists
# @param t a list of lists of integers
# @return the sum of all the elements of the nested lists
def nested_sum(t):
    total = 0
    for i in range (len(t)):
        total += sum(t[i])
    return total

# Call the nested_sum function and print it
print(nested_sum([[1, 2], [5, 4], [6]]))
