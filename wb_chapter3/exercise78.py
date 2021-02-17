##
# Collatz Conjecture
#

# Read a positive integer from user
n = int(input("Please, enter a positive integer: "))

# Check if n is a positive integer
# For the positive n given, print each term of the sequence
while n > 0:
    print(n)
    while True:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            if n == 1:
                break
            else:
                n = n * 3 + 1
            print(n)
    
    n = int(input("Please, enter the next positive integer: "))