##
# Display the name of the individuals on USA banknotes
#

# Read the denomination of a banknote from the user
banknote = input("Enter the denomination of a banknote in $: ")

# Determine if the entered banknote has an individual printed on it
if banknote == "$1":
    individual = "George Washington"
elif banknote == "$2":
    individual = "Thomas Jefferson"
elif banknote == "$5":
    individual = "Abraham Lincoln"
elif banknote == "$10":
    individual = "Alexander Hamilton"
elif banknote == "$20":
    individual = "Andrew Jackson"
elif banknote == "$50":
    individual = "Ulysses S. Grant"
elif banknote == "$100":
    individual = "Banjamin Franklin"
else:
    individual = ""

# Display the result
if individual == "":
    print("Such a banknote doesn't exist")
else:
    print(banknote, "has", individual, "printed on it")