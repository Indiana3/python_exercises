##
# Simulate 1000 Bingo games and report the minimum,
# maximum and avarage number of calls that must be made to win
#
from random import shuffle
from exercise146 import bingoCard, printBingoCard
from exercise147 import isWinningCard

# Set the number of games to paly
NUM_GAMES = 1000

# Numbers range of a Bingo card
BINGO_NUMBERS = 75

# Initialize a dictionary to store the number of calls
# for each game
games = {}

# For each Bingo game
for game in range(NUM_GAMES + 1):
    # Create an empty list to store calls
    calls = []

    # Create a list of calls
    for i in range(1, BINGO_NUMBERS + 1):
        calls.append(i)

    # Shuffle Bingo calls
    shuffle(calls)

    # Generate a Bingo card
    card = bingoCard()

    # Before starting the game, no calls have been made
    num_calls = 0

    # Until you don't get a winning line
    while isWinningCard(card) == False:
        # Call out a number from the list
        extracted_num = calls.pop()
        # Check if it's in the Bingo card
        # and replace it with 0
        for value in card.values():
            for i in range(len(value)):
                if value[i] == extracted_num:
                    value[i] = 0
        num_calls += 1

    # Each game maps to the number of calls needed to win
    games[game] = num_calls

# Find the minimum number of calls to win
min_calls = min(games.values())
print("The minimum number of calls is {}".format(min_calls))

# Find the maximum number of calls to win
max_calls = max(games.values())
print("The maximum number of calls is {}".format(max_calls))

# Find the avarage number of calls to win
total = 0
for value in games.values():
    total += value
avarage = total / len(games)
print("The avarage number of calls is {}".format(round(avarage)))   

