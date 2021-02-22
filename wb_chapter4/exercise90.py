##
# Display all the verses of the song "The Twelve Days of Christmas"
#
from exercise89 import to_ordinal_num

## Add a new verse of the song
# @param n the number of the verse
# return the new verse corresponding to n
#

def add_verse(n):
    if n == 1:
        return "And a partridge in a pear tree."
    elif n == 2:
        return "Two turtle doves,"
    elif n == 3:
        return "Three French hens,"
    elif n == 4:
        return "Four calling birds,"
    elif n == 5:
        return "Five gold rings,"
    elif n == 6:
        return "Six geese a laying,"
    elif n == 7:
        return "Seven swans a swimming,"
    elif n == 8:
        return "Eight maids a milking,"
    elif n == 9:
        return "Nine ladies dancing,"
    elif n == 10:
        return "Ten lords a leaping,"
    elif n == 11:
        return "Eleven pipers piping,"
    elif n == 12:
        return "Twelve drummers drumming,"

NUM_VERSES = 12

# Display the first verse
print()
print("On the first day of Christmas")
print("my true love sent to me: ")
print("A partridge in a pear tree.")

# Display the following verses
for n in range (2, NUM_VERSES + 1):
    print()
    print("On the", to_ordinal_num(n), "day of Christmas")
    print("my true love sent to me: ")
    while n > 0:
        print(add_verse(n))
        n = n - 1

    


    
