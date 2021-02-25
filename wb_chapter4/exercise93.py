##
# Center a string in the terminal window
#

# Store the width of a window as constant
WIDTH = 80

## Center a string in the terminal window
# @param s a string
# @param w the width of the window in characters
# @return a string with the same leading spaces from
# left and right margin
#
def stringCentered(s, w):
    if len(s) >= w:
        return s
    else:
        leading_spaces = " " * (abs(len(s) - w) // 2)
        s_centered = leading_spaces + s
        return s_centered

# Print some centered strings
def main():
    print(stringCentered("L'esercito di terracotta", WIDTH))
    print(stringCentered("L'arca dell'alleanza", WIDTH))
    print(stringCentered("Il faro di Alessandria", WIDTH))
    print(stringCentered("I papiri di Ossirinco", WIDTH))

# Call the main function
main()
