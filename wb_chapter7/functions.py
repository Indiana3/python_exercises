import os

def filePath(dir):
    all_paths = []
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        all_paths.append(path)
    return all_paths

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