##
# Find the most popular boy's name and the most popular girl's name in
# a given period of time
#
from exercise163 import all_paths

# Read the period of time from the user
ab, ad = input("Please, enter a time period (from 1900 to 2012): ").split()
ab, ad = int(ab), int(ad)

# Create a list with all the years to analyze
time_period = [i for i in range(ab, ad+1)]

# Create an empty list to add the absolute paths
# pointing to the files to analyze
to_analyze_files = []

# For each year in the time period list
for i in range(len(time_period)):
    # Convert the integer year to a string
    year = str(time_period[i])
    # For each path
    for j in range(len(all_paths)):
        # Check if the year is included in the file path string
        if year in all_paths[j]:
            # Select the file with boy's names and the file with girl's names
            paths = [all_paths[j], all_paths[j+1]]
            # Add the files to the files to analyze 
            to_analyze_files.extend(paths)
            break

# Create a list for boy's names
boy_names = []

# Create a list for girl's names
girl_names = []

# For each file to analyze
for path in to_analyze_files:
    # Open the file
    fl = open(path, "r")
    # Read the first line and remove EOL chars
    line = fl.readline().strip()
    # Save the name in a variable
    name = line.split()[0]
    # If the file contains boy's names
    if "Boys" in path:
        # Add it to the boy's names list
        boy_names.append(name)
    # If the file contains girl's names
    elif "Girls" in path:
        # Add it to the girl's names list
        girl_names.append(name)
    # Close the file
    fl.close()

# Display the result
for i in range(len(time_period)):
    print("In the {}, the most popular boy's name was {}, the most popular girl's name was {}".format(time_period[i], boy_names[i], girl_names[i]))
    