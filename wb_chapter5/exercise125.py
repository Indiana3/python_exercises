##
# Create a deck of 52 cards and shuffle it
# Display the shuffled deck
#
from random import randrange

## Create a deck of 52 cards: each card is represented
# with 2 characters.
# The first one is a value from 2 to 9 plus "T", "J", "Q", "K" and "A"
# (that stand for 10, Jack, Queen, King and Ace).
# The second one is a lowercase lettere representing one of the four suits:
# "s" for spades, "h" for hearths, "d" for diamonds, "c" for clubs
# @return a list with all the cards 
#
def createDeck():
    # Create a list for suits and one for values
    suits = ["s", "h", "d", "c"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T",
    "J", "Q", "K", "A"]
    # Create a list to store the cards
    cards = []
    # Each suit has a value between 2 and A
    for i in range(len(suits)):
        for j in range(len(values)):
            # Value comes before suit
            card = values[j] + suits[i]
            # Store each card in the list
            cards.append(card)
    return cards

## Shuffle the deck previous created
# @param t a list of cards
# @return the list of cards shuffled
#
def shuffle(t):
    # Copy the list passed as parameter
    v = t[:]
    # Move each card to a random position in the list
    for i in range(len(v)):
        # Pick a random index between the current index and
        # the end of the list
        j = randrange(i, len(v))
        # Swap the current card with the one at the random index
        temp = v[i]
        v[i] = v[j]
        v[j] = temp
    return v

# Create a deck of 52 cards and display it before and after shuffling
def main():
    deck = createDeck()
    shuffled_deck = shuffle(deck)
    print("Deck: ")
    for card in deck:
        print(" ", card)
    print("Shuffled deck: ")
    for card in shuffled_deck:
        print(" ", card)

# Call the main function
if __name__ == "__main__":
    main()