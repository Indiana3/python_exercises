## Read an integer and display its value in English words
# @param number an integer from 0 to 999
# @return a string containing the English words for that integer
#
def integersToWords(number):
    ## Each digit maps to its English word
    # Use for units and hundreds
    units = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
    "6": "six", "7": "seven", "8": "eight", "9": "nine" } 

    # For numbers from 10 to 19
    teen_numbers = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
    "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}

    # For dozens from 20 to 90
    dozens = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
    "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}

    ## Check how many digits there are in n
    # 1 digit (units)
    if len(number) == 1:
        return units[number]
    # 2 digits (units and dozens)
    elif len(number) == 2:
        # n is equal/greater than 10 and equal/lower than 19 
        if number >= "10" and number <= "19":
            return teen_numbers[number]
        else:
            # Units equal to 0
            if number[1] == "0":
                return dozens[number[0]]
            # Units from 1 to 9
            return dozens[number[0]] + " " + units[number[1]]
    # 3 digits (units, dozens and hundreds)
    elif len(number) == 3:
        # Dozens and units equal to 0
        if number[1:] == "00":
            return units[number[0]] + " hundred"
        # Dozens equal to 0, units from 1 to 9
        elif number[1:] >= "01" and number[1:] <= "09":
            return units[number[0]] + " hundred" + " and " + units[number[2]] 
        # Dozens and units correspond to a number equal/greater than 10 and equal/lower than 19
        elif number[1:] >= "10" and number[1:] <= "19":
            return units[number[0]] + " hundred" + " " + teen_numbers[number[1:]]
        # Dozens and units correspond to a number from 20 to 99
        else:
            # Units equal to 0
            if number[2] == "0":
                return units[number[0]] + " hundred" + " " + dozens[number[1]]
            # Units Units from 1 to 9
            return units[number[0]] + " hundred" + " " + dozens[number[1]] + " " + units[number[2]]

# Read an integer from user as string and display
# its value in English words
def main():
    n = input("Please, enter an integer between 0 and 999: ")
    print("The English words for %s is/are: %s" %(n, integersToWords(n)))

# Call the main function
if __name__ == "__main__":
    main()




