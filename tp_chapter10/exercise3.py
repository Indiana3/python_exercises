## Delete the first and the last elements from a list
# @param t a list
# @return a new list without the first and last elements
def middle(t):
    t1 = []
    for i in range (0, len(t)):
        if i == 0 or i == len(t) - 1:
            continue
        t1.append(t[i])
    return t1

# Assign a list to t 
# Call the middle function
# Print list t and the new list t1
t = [2, 3, 4, 5, 6]
t1 = middle(t)
print(t)
print(t1)