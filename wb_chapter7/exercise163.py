##
# Find the most popular boy and girl names
# between 1900 and 2012
#
import os

## Create a list of absolute paths of files in a given directory
# param dir the directory absolute path
# return the file absolute paths list 
#
def filePath(dir):
    all_paths = []
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        all_paths.append(path)
    return all_paths

# Join the current directory absolute path with the name of
# the directory where files are contained
baby_names = os.path.join(os.getcwd(), "baby_names")

# Store the list of paths in a variable
all_paths = filePath(baby_names)

if __name__ == "__main__":
    # Create 2 empty list to store boy and girl names
    boy_names = []
    girl_names = []

    # For each path in the list of paths
    for path in all_paths:
        # Open the file
        fl = open(path, "r", encoding="utf-8")
        # Read the first line and remove the EOL characters
        line = fl.readline().strip()
        # Store the name in a variable
        name = line.split()[0]
        # Check if the path points to a file containing boy names
        if "Boys" in path:
            # Check if the name is already in the appropriate list
            if name not in boy_names:
                # Add it to the list
                boy_names.append(name)
        # Check if the path points to a file containing girl names
        elif "Girls" in path:
            # Check if the name is already in the appropriate list
            if name not in girl_names:
                # Add it to the list
                girl_names.append(name)
        # Close the file
        fl.close()

    # Print the most popular boy names
    for name in boy_names:
        print(name)

    print("\n" * 3)

    # Print the most popular girl names
    for name in girl_names:
        print(name)

