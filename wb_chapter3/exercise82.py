##
# Decimal to Binary
#

# Read the binary number from user
num = int(input("Please, enter a decimal number: "))

# Convert into binary digits
result = ""
q = num

# For num = 0
r = q % 2
result = str(r) + result
q = q // 2

# For integers greater than 0
while q > 0:
    r = q % 2
    result = str(r) + result
    q = q // 2

# Display the binary number
print(result)