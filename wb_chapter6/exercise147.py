##
# Show with examples winning and not winninf Bingo cards
#
from random import randint
from exercise146 import bingoCard, printBingoCard
# Store the keys of card dictionary in a list
keys = ["B", "I", "N", "G", "O"]

## Determine is a Bingo card is winning or not
# @param card a dictionary representing a Bingo card
# @return True if the card contains a line of 5 zeros (horizontal, vertical or diagonal);
# False otherwise
#
def isWinningCard(card):
    # To be winning, the sum of the numbers in a line
    # (horizontal, vertical or diagonal) have to be 0
    
    # Start with a variable total equal to 0
    total = 0
    
    # Sum all the 5 numbers in each horizontal line and before
    # moving to the next line, check if the sum is 0
    for i in range(5):
        for value in card.values():
            total += value[i]
        if total == 0:
            return True
        # Before starting with the following line, reset total to 0
        total = 0
    
    # Sum all the 5 numbers in each vertical line and before
    # moving to the next line, check if the sum is 0
    for value in card.values():
        total += sum(value)
        if total == 0:
            return True
        # Before starting with the following line, reset total to 0
        total = 0

    # Sum all the 5 numbers in each diagonal line and before
    # moving to the next line, check if the sum is 0
    # Initialize a counter for keys list
    j = 0
    # Inizialize a counter for the lists in card dictionary
    i = 0
    # Sum each number of the diagonal line from left-top to right-bottom
    while j < len(keys) and i < 5:
        total += card[keys[j]][i]
        j = j+1
        i = i+1
    if total == 0:
        return True
    
    # Reset total to 0
    total = 0
    # Reset counter for keys list to 0
    j = 0
    # Reset counter for lists in card dictionary to 4
    i = 4
    # Sum each number of the diagonal line from left-bottom to right-top
    while j < len(keys) and i >= 0:
        total += card[keys[j]][i]
        j = j+1
        i = i-1
    if total == 0:
        return True

    return False

# Show some examples of winning Bingo cards
def main():
    # Create a Bingo card
    card1 = bingoCard()
    # All the numbers of the first horizontal line have been crossed out 
    for value in card1.values():
        value[0] = 0
    # Display the result
    if isWinningCard(card1):
        print("This Bingo card is winning")
        printBingoCard(card1)
        print()

    # Create a Bingo card
    card2 = bingoCard()
    # All the numbers of the first vertical line have been crossed out 
    for i in range(len(card2["B"])):
        card2["B"][i] = 0
    # Display the result
    if isWinningCard(card2):
        print("This Bingo card is winning")
        printBingoCard(card2)
        print()

    # Create a Bingo card
    card3 = bingoCard()
    # Initialize a counter for keys list
    j = 0
    # Inizialize a counter for the lists in card dictionary
    i = 0
    # All the numbers of the right-top left-bottom diagonal have been crossed out 
    while j < len(keys) and i < 5:
        card3[keys[j]][i] = 0
        j = j+1
        i = i+1
    # Display the result
    if isWinningCard(card3):
        print("This Bingo card is winning")
        printBingoCard(card3)
        print()

    # Create a Bingo card
    card4 = bingoCard()
    # This card has not winning lines
    for i in range(3):
        card4["B"][i] = 0
    # Display the result
    if not isWinningCard(card4):
        print("This Bingo card is not winning")
        printBingoCard(card4)
        print()

# Call the main function
if __name__ == "__main__":
    main()



