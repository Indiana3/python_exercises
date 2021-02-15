##
# For n from 1 to 100, display:
# Fizz if n is divisble by 3
# Buzz if n is divisble by 5
# Fizz-Buzz if n is divisible by 3 and 5
# 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz-Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print("{}".format(i))
      

