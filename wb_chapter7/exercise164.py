##
# Check if there are gender neutral names in a given year
#
from exercise163 import all_paths

## Find the absolute paths of files pointing to
# the baby names in a given year
# @param all_paths a list of absolute paths
# @param year a year from 1900 to 2012 passed as string
# @return a tuple with the absolute paths pointing to
# the boy names file and the girl names file of that year
#
def bornInAGivenYear(all_paths, year):
    for i in range(len(all_paths)):
        if year in all_paths[i]:
            boys = all_paths[i]
            girls = all_paths[i+1]
            break
    return (boys, girls)

## Read the names in a file and add them in a set
# @param path the absolute path pointing to a file
# @return a set of names
#
def setOfNames(path):
    set_of_names = set()
    fl = open(path, "r", encoding="utf-8")
    line = fl.readline().strip()
    while line != "":
        name = line.split()[0]
        set_of_names.add(name)
        line = fl.readline().strip()
    fl.close()
    return set_of_names

# Read the year from the user
year = input("Please, enter a year (between 1900 and 2012): ")

# Check if the year is out of range (1900-2012) and
# print an error message
if int(year) < 1900 or int(year) > 2012:
    print("Sorry, no data available")
# Store the file paths in a variable
else:
    paths = bornInAGivenYear(all_paths, year)

# For each file
for path in paths:
    # Create a set of names for boys
    if "Boys" in path:
        boy_names = setOfNames(path)
    # Create a set of names for girls
    elif "Girls" in path:
        girl_names = setOfNames(path)

# Check if there are gender neutral names
neutral_names = boy_names & girl_names

# Display the result
if len(neutral_names) != 0:
    print("The gender neutral names in the", year, "are: ")
    for name in neutral_names:
        print(name)
else:
    print("None") 





