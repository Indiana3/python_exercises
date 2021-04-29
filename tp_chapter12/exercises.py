## Sum a variable number of integers and floats
# @param *args a variable number of integer and float types
# @return their summation
#
def sum_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# Call the function and show its result with an example
print(sum_all(2, 3, 4, 5))








