##
# Convert amounts in greater units of measure
#

## Express a number of units with the greatest possible unit of measure
# (cup, tablespoon, teaspoon)
# @param units the number of units
# @param unit_of_measure the unit of measure used
# @return a string with the same amount expressed with the
# greatest possible unit of measure
def greatestPossibleUnit(units, unit_of_measure):
    #
    TEASPOONS_IN_TABLESPOON = 3
    TABLESPOONS_IN_CUP = 16
    # Convert the number of units if the unit of measure is teaspoon
    if unit_of_measure == "teaspoon":
        teaspoons = units % TEASPOONS_IN_TABLESPOON
        to_greater_units = units // TEASPOONS_IN_TABLESPOON
        tablespoons = to_greater_units % TABLESPOONS_IN_CUP
        cups = to_greater_units // TABLESPOONS_IN_CUP
        return "{} teaspoons, {} tablespoons, {} cups".format(teaspoons, tablespoons, cups)
    # Convert the number of units if the unit of measure is tablespoon
    elif unit_of_measure == "tablespoon":
        tablespoons = units % TABLESPOONS_IN_CUP
        cups = units // TABLESPOONS_IN_CUP
        return "{} tablespoons, {} cups".format(tablespoons, cups)
    # Convert the number of units if the unit of measure is cup
    elif unit_of_measure == "cup":
        return "{} cups".format(units)

# Read the number of units and their unit of measure from the user
# Display that number of units with the greatest unit of measure
def main():
    units = int(input("Please, enter a number of units: "))
    unit_of_measure = input("Please, enter the corresponding unit of measure"\
        "(teaspoon, tablespoon, cup): ")
    print(greatestPossibleUnit(units, unit_of_measure))

# Call the main function
main()
