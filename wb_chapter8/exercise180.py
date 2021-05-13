##
# Compute the edit distance between 2 strings
#

## Compute the minimum number of steps to transform
# one string into another string (edit distance) 
# @param s a string
# @param t another string
# @return a positive integer representing 
# the edit distance
#
def stringEditDistance(s, t):
    # Base case
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    else:
        # Recursive case
        cost = 0
        if s[-1] != t[-1]:
            cost = 1
        d1 = stringEditDistance(s[:-1], t) + 1
        d2 = stringEditDistance(s, t[:-1]) + 1
        d3 = stringEditDistance(s[:-1], t[:-1]) + cost
        return min(d1, d2, d3)

# Read 2 strings from user and display the result
def main():
    s = input("Please, enter a string: ")
    t = input("Please, enter a second string: ")
    edit_distance = stringEditDistance(s, t)
    print("The edit distance between '%s' and '%s' is %d" % (s, t, edit_distance))

# Call the main function
if __name__ == "__main__":
    main()
