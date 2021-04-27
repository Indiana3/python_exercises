from random import randint

NUMS_PER_LETTER = 15

## Create a random Bingo Card
# @param None
# @return a dictionary mapping from letters B, I, N, G, O 
# to the lists of five random numbers under each letter
#
def bingoCard():
    card = {}
    # The range of integers available for the current letter
    lower = 1
    upper = NUMS_PER_LETTER
    # For each of the following letter
    for letter in ["B", "I", "N", "G", "O"]:
        # Start with an empty list for each letter
        card[letter] = []
        # Keep generating random numbers until we have 5 unique ones
        while len(card[letter]) != 5:
            number = randint(lower, upper)
            # Ensure that we don't include any duplicate number
            if number not in card[letter]:
                card[letter].append(number)
        # Update the range available for the next letter
        lower = lower + NUMS_PER_LETTER
        upper = upper + NUMS_PER_LETTER
    
    return card

## Display the Bingo card
# @param card a dictionary
# @return None
#
def printBingoCard(card):
    # Print all the letters one next to the other
    for letter in ["B", "I", "N", "G", "O"]:
        print("%8s" % (letter), end="")
    print()
    # On each line, print the nth random number 
    # for that letter. Each letter has 5 numbers
    for i in range(5):
        for value in card.values():
            print("%8i" % (value[i]), end="")
        print()

# Display a random Bingo card
def main():
    card = bingoCard()
    printBingoCard(card)

# Call the main function:
if __name__ == "__main__":
    main()
