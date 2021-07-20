##
# Find all the distinct baby names from 1900 to 2012
#
from exercise163 import all_paths
from exercise164 import setOfNames

# Create an empty set for boy's names
boy_names = set()

# Create an empty set for girl's names
girl_names = set()

# For each file
for path in all_paths:
    # Store all the boy's names for that year in a set 
    if "Boys" in path:
        boy_names_in_a_year = setOfNames(path)
        # Add these names to the set storing boy's names of previous years
        boy_names = boy_names.union(boy_names_in_a_year)
    # Store all the girl's names for that year in a set
    elif "Girls" in path:
        girl_names_in_a_year = setOfNames(path)
        # Add these names to the set storing girl's names of previous years
        girl_names = girl_names.union(girl_names_in_a_year)

# Display all the distinct boy's names
for name in boy_names:
    print(name)

print("\n")

# Display all the distinct girl's names
for name in girl_names:
    print(name)       