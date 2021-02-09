##
# Simulates a spin of a roulette wheel
#
from random import choice

# Display the sorted number
alpha_num = ["00", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

sorted_num = choice(alpha_num)
print("The spin resulted in", sorted_num, "...")

# Display the colour payout
print("Pay", sorted_num)
if sorted_num % 2 == 1 and sorted_num >= 1 and sorted_num <= 9 or \
    sorted_num % 2 == 0 and sorted_num >= 12 and sorted_num <= 18 or \
    sorted_num % 2 == 1 and sorted_num >= 19 and sorted_num <= 27 or \
    sorted_num % 2 == 0 and sorted_num >= 30 and sorted_num <= 36:
    print("Pay Red") 
elif sorted_num == 0 or sorted_num == "00":
    pass
else:
    print("Pay Black")

# Display if sorted_num is even or odd

if sorted_num % 2 == 0:
    print("Pay Even")
else:
    print("Pay Odd")

# Display lower numbers vs upper numbers

if sorted_num > 0 and sorted_num <= 18:
    print("Pay 1 to 18")
else:
    print("Pay 19 to 36")
