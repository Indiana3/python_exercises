from exercise9 import list_builder

# Generate a list of word
t = list_builder('../tp_chapter8/words.txt')

## Check if a word is in the list
# @param t a sorted list
# @param value the word we wnat to check
# @param n the max number of times you have to cut the list before returning
# @return True if the word is the list; False otherwise
def in_bisect(t, value, n):
    half = len(t) // 2
    for _ in range (n):
        if value == t[half]:
            return True
        elif value < t[half]:
            t = t[:half]
        elif value > t[half]:
            t = t[half:]
        half = half // 2
    return False

# Call in_bisect function and print the risult
print(in_bisect(t, "abatis", 17))