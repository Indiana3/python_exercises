##
# Sum a collection of number
#

# Read a number from the user
num = input("Please, enter a number: ")

# Start with total equal to 0
total = 0

# While the user don't enter a blank line
while num != "":
    try:
        # Convert the str value into a numeric value
        num = float(num)
        # Add it to previous sum
        total += num
        # Display the sum
        print("The sum of the numbers entered so far is: ", total)
    except:
        # Print an error message if the user entered a non numeric value
        print("You entered a non numeric value")
    
    # Ask for the next number
    num = input("Please, enter another number: ")

# Display the grand total
print("The grand total is: ", total)