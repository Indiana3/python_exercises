##
# Multiplication Table from 1 times 1 up to and
# including 10 times 10
#

# Print 2 margin spacings for the row of labels
print("  ", end="")
# Print the row of labels
for i in range(1, 11):
    print("%4i" % i, end="")
print()

# Print the left side labels and all the multiplications
for i in range(1, 11):
    print("%2i" % i, end="")
    for j in range(1, 11):
        print("%4i" % (j * i), end="")
    print()