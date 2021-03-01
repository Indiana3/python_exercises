##
# Determine if an integer is a prime number
#

## Check if an integer is a prime number
# @param n an integer number
# @return True if n is a prime number, return False otherwise
def isPrime(n):
    if n <= 1:
        return False
    
    # Check each number from 2 up to but not including n to se if it divides evenly into n
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

# Determine if a number entered by the user is prime
def main():
    n = int(input("Please, enter an integer: "))
    if isPrime(n):
        print("{} is a prime number".format(n))
    else:
        print("{} is not a prime number".format(n))

# Call the main function
if __name__ == "__main__":
    main()