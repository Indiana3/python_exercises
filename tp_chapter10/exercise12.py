## Check if two words in a list are interlocked;
# that is, taking alternative letters from each
# they form a third word in the list
#
from exercise9 import list_builder
from bisect import bisect_left

## Check if 2 lists have the same length
# @param t the first list
# @param v the second list
# @return True if they have the same length; False otherwise
def has_same_length(t, v):
    if len(t) == len(v):
        return True
    return False

## Create an interlock word
# @param t a list whose elements are letters
# @param v a list whose elements are letters
# @param list_length the length of list t and v (must be the same)
# @return a string taking alternative letters from the 2 lists
def interlock(t, v, list_length):
    z = []
    for i in range(list_length):
        z.append(t[i])
        z.append(v[i])
        interlock_word = "".join(z)
    return interlock_word

def main():
    # Import a file .txt with a list of word
    t = list_builder('../tp_chapter8/words.txt')
    # Compare each element of t with the following
    for i in range(len(t) - 1):
        first_word_list = list(t[i])
        for j in range(i+1, len(t)):
            second_word_list = list(t[j])
            # Create an interlock word only from 2 words with same length
            if has_same_length(first_word_list, second_word_list):
                list_length = len(first_word_list)
                interlock_word = interlock(first_word_list, second_word_list, list_length)
                # Determine the position the word checked would have in the sorted list
                position = bisect_left(t, interlock_word)
                # Check if the interlock word is in list t
                if interlock_word == t[position]:
                    print("%s is in the list" %interlock_word)

# Call the main function
if __name__ == "__main__":
    main()