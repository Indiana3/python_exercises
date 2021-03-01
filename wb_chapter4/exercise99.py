##
# Determine the first prime number larger than some integer n
#
from exercise98 import isPrime

# Determine the first prime number larger than n
# @param n an integer
# @return the first prime number larger than n
#
def nextPrime(n):
    # Check each number greater than n until find a prime number
    n = n + 1
    while isPrime(n) == False:
        n = n + 1
    return n

# Determine the next prime number of the integer entered by the user
def main():
    n = int(input("Please, enter an integer number: "))
    print("The first prime number greater than {} is {}".format(n, nextPrime(n)))

# Call the main function
main()