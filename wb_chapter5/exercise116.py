##
# Compute and display all the perfrct numbers betwen 1 and 10000
#
from exercise115 import proper_divisors

## Determine if a positive integer is a perfect number
# @param n a positive integer
# @return True if n is a perfect number; False otherwise
# 
def is_perfect(n):
    divisors = proper_divisors(n)
    if n == sum(divisors):
        return True
    return False

# Identify and display all of the perfect numbers between 1 and 10000
def main():
    print("The perfect numbers between 1 and 10000 are: ")
    for i in range(1, 10001):
        if is_perfect(i):
            print(i)

# Call the main function
if __name__ == "__main__":
    main()