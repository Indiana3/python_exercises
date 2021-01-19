##
# Compute the BMI (Body Mass Index)
#

# Read the height and weight from the user
print("Please, enter: ")
height = float(input("your height: "))
height_unit = input("inches (inc) or meters (m)? ")
weight = float(input("your weight: "))
weight_unit = input("pounds (p) or kilograms (kg)? ")

# Lowercasing units
height_unit = height_unit.lower()
weight_unit = weight_unit.lower()

# Compute the BMI
if height_unit[-1] == "c" and weight_unit[-1] == "p":
    bmi = weight / (height ** 2) * 703

elif height_unit[-1] == "m" and weight_unit[-1] == "g":
    bmi = weight / (height ** 2)

else:
    print ("Enter values with the right units")
    quit()

# Display BMI
print("Your BMI is %.2f" % bmi)




