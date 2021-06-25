from exercise2 import all_anagrams
import shelve

## Store an anagram dictionary in a "shelf"
# @param dict an anagram dictionary
# @return a shelf object
#
def store_anagrams(d):
    with shelve.open("anagrams", "c") as db:
       for key, value in d.items():
           db[key] = value
    return db

if __name__ == "__main__":
    anagram_sets = all_anagrams("../tp_chapter8/words.txt")

            


    