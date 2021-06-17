from bisect import bisect_left
from random import randint

# Step 0
# Create a dictionary with words as keys and their frequencies as values
d = {
    "love" : 2,
    "meditation" : 3,
    "football" : 1,
    "nature": 5,
    "green" : 10,
    "farm" : 2,
    "and" : 5,
    "cats" : 4
}

# Step 1
# Use keys to get a list of the words in the book
word_ls = []
for key in d:
    word_ls.append(key)
print(word_ls)

# Step 2
# Build a list that contains all the word frequencies
freq_ls = []
for value in d.values():
    freq_ls.append(value)
print(freq_ls)

# Step 2.1
# Build a list that contains the cumulative sum of the word frequencies. 
# The last item in this list is the total number of words in the book, n
cumfreq = [freq_ls[0]]
for i in range(1, len(freq_ls)):
    cumfreq.append(freq_ls[i] + cumfreq[i-1])
print(cumfreq)

# Step 3
# Choose a random number from 1 to n. Use a bisection search to
# find the index where the random number would be inserted in the cumulative sum
index = bisect_left(cumfreq, randint(1, cumfreq[-1]))
print(index)

# Step 4
# Use the index to find the corresponding word in the word list
print(word_ls[index])

