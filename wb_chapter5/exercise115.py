##
# Read a positive integer and compute all its proper divisors
#

## Find the proper divisors of a positive integer
# @param n a positive integer
# @return a list with all the positive integers
def proper_divisors(n):
    divisors = []
    for i in range (1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Read a positive integer from user and display its proper divisors
def main():
    num = int(input("Please, enter a positive integer: "))
    if num <= 0:
        print("You didn't enter a positive number")
    else:
        print("The proper divisors of {} are: {}".format(num, proper_divisors(num))) 

# Call the main function
if __name__ == "__main__":
    main()