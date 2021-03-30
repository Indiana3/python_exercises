##
# Deal out four hands of five cards each
#
from exercise125 import createDeck, shuffle

## Generate x hands of cards with n cards per hand
# @param num_hands the number of hands dealt out
# @param num_cards the number of cards per hand
# @param shuffled_deck a list with all the cards shuffled
# @return a list containing all of the hands
#
def deal(players, cards_per_hand, shuffled_deck):
    # Before dealing the hands, each player has no cards
    hands = []
    # In hands list, store a number of sublists equal to the number of players
    for _ in range(players):
        hands.append([])
    # For the number of cards in each hand
    for _ in range(cards_per_hand):
        # For each player
        for i in range(players):
            # Remove the top card of the deck
            dealt_card = shuffled_deck.pop(0)
            # Add it to the player's hand 
            hands[i].append(dealt_card)
    return hands

def main():
    # Generate a deck of cards and shuffle it
    deck = createDeck()
    shuffled_deck = shuffle(deck)

    # Display all of the hands of cards
    hands = deal(4, 5, shuffled_deck)
    for hand in hands:
        print(hand)
    
    # Display the cards remaining in the deck after cards dealing
    print(shuffled_deck)

# Call the main function
if __name__ == "__main__":
    main()