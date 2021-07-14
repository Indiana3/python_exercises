##
# Read a file containing information about chemical elements,
# store them in data structure/s
# and display them to the user
#

# Open the file
fl = open("chemical_elements.txt", "r", encoding="utf-8")

# Create an empty list to store atomic numbers
atomic_num = []
# Create an empty list to store element symbols
elem_symbol = []
# Create an empty list to store element names
elem_name = []

# Read each line of the file
for line in fl:
    # Remove EOL chars from the line
    line = line.strip()
    # Split line in a list with a "," as separator
    data = line.split(",")
    # Add atomic number to its list
    atomic_num.append(data[0])
    # Add element symbol to its list
    elem_symbol.append(data[1])
    # Add element name to its list
    elem_name.append(data[2])

# Close the file   
fl.close()

# Read an input from the user
inp = input("Please, enter an atomic number, symbol or name of a chemical element: ")

# Until the user enter a blank line
while inp != "":
    try:
        # Check if the input is in atomic number list
        position = atomic_num.index(inp)
        # Display the corresponding element symbol, name and number of protons (equal to atomic number)
        print(elem_symbol[position], elem_name[position], atomic_num[position])
    except:
        inp = inp.capitalize()
        try:
            # Check if the input is in chemical symbol list
            position = elem_symbol.index(inp)
            # Display the number of protons and the element name 
            print(atomic_num[position], elem_name[position])
        except:
            try:
                # Check if the input is in chemical name list
                position = elem_name.index(inp)
                # Display the number of protons and the element symbol
                print(atomic_num[position], elem_symbol[position])
            except:
                # Display an error message
                print("There's no track of this chemical element")
    
    # Ask for another input
    inp = input("Please, enter another atomic number, symbol or name of a chemical element: ")


