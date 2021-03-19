from exercise9 import list_builder

## Check if a word is in the list
# @param t a sorted list
# @param value the word we want to check
# @param n the max number of times you have to cut the list before returning
# @return True if the word is the list; False otherwise
def in_bisect(t, value, n = 17):
    half = len(t) // 2
    for _ in range (n):
        if value == t[half]:
            return True
        elif value < t[half]:
            t = t[:half]
        elif value > t[half]:
            t = t[half:]
        half = len(t) // 2
    return False

# Call in_bisect function and print the risult
def main():
    # Generate a list of word
    t = list_builder('../tp_chapter8/words.txt')
    print(in_bisect(t, "abatis"))

# Call the main function
if __name__ == "__main__":
    main()