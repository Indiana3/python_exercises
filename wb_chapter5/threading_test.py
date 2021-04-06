from exercise125 import createDeck, shuffle
import threading
import time

# Create a deck of 52 cards
deck = createDeck()

# Shuffle the deck and display what you get.
def shuffleDeck(deck):
    print(shuffle(deck))

## Using threading module

# Create an empty list to store all threads
threads = []

# Time starts
start = time.time()

# Each thread is a deck shuffling
# Repeat it for 3 times
for _ in range(3):
    t = threading.Thread(target=shuffleDeck, args=[deck])
    t.start()
    # Add each thread to threads list
    threads.append(t)

# Before going on with execution, all threads must end
for i in range(len(threads)):
    threads[i].join()

# Time ends
end = time.time()
print("Shuffling a deck four times take %f seconds" %(end-start))

## Sequential execution

# Start time
start = time.time()

# Repeat deck shuffling for 3 times
for _ in range(3):
    shuffleDeck(deck)

# Time ends
end = time.time()
print("Shuffling a deck four times take %f seconds" %(end-start))


