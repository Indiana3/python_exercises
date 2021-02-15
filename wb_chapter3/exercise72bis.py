##
# For n from 1 to 100, display:
# Fizz if n is divisble by 3
# Buzz if n is divisble by 5
# Fizz-Buzz if n is divisible by 3 and 5
# 

number = 1
final_number = 100

while number <= final_number:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz-Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("{}".format(number))
    number = number + 1