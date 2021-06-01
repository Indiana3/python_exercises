##
# Display all the chemical elements that can be spelled
# using only chemical symbols
#

## Determine if a word can be spelled using only a set of symbols
# @param s a word
# @param t a list containing symbols
# @return a string with the symbols used to spell the given word
#
def spelling(s, t):
    # Base case
    if s == "":
        return ""
    
    # Recursive case
    elif s[:3] in t:
        return s[:3].capitalize() + spelling(s[3:], t)
    elif s[:2] in t:
        return s[:2].capitalize() + spelling(s[2:], t)
    elif s[:1] in t:
        return s[:1].capitalize() + spelling(s[1:], t)
    else:
        return ""

# Store the main program in a main function
def main():
    # Open the file "element_symbols.txt" 
    fl = open("element_symbols.txt", "r")
    
    # Store all the lines in a list
    lines = fl.readlines()
    
    # Create 2 lists: one to store chemical symbols as strings; the other
    # to store elements as strings
    symbols = []
    elements = []
    
    # Remove the trailing white spaces from each line
    # and add symbols and elements to their lists 
    for line in lines:
        line = line.strip()
        line = line.split(",")
        symbols.append(line[1])
        elements.append(line[2])

    # Turn all symbols to lowercase chars
    symbols_lower = []
    for symbol in symbols:
        symbols_lower.append(symbol.lower())

    # Turn all the elements to lowercase chars
    elements_lower = []
    for element in elements:
        elements_lower.append(element.lower())

    # Create an empty dictionary to store elements as keys
    # and spellings as values
    chemical_spelling = {}

    # Each spelling is computed using spelling function
    for element in elements_lower:
        chemical_spelling[element] = spelling(element, symbols_lower)

    # Display only the elements that can be spelled completly
    for element, sp in chemical_spelling.items():
        if len(element) == len(sp):
            print("{} can be spelled as {}".format(element.capitalize(), sp))

# Call the main function
if __name__ == "__main__":
    main()



