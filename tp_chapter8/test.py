import os


def over_20_chr():
    fin = open("C:/Users/Lorenzo/Desktop/Informatica/tomorrowDevs/learn_python/python_exercises/tp_chapter8/words.txt")
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

def has_e():  
    fin = open(os.path.abspath('words.txt'))
    counter = 0
    for line in fin:
        word = line.strip()
        for c in word:
            if c == 'e':
                print(word)
                counter = counter + 1
                break
    print(counter)

def has_r():  
    fin = open(os.path.abspath('words.txt'))
    counter = 0
    for line in fin:
        word = line.strip()
        for c in word:
            if c == 'r':
                print(word)
                counter = counter + 1
                break
    print(counter)

def words_counter():  
    fin = open(os.path.abspath('words.txt'))
    words_num = 0
    for line in fin:
        word = line.strip()
        print(word)
        words_num = words_num + 1
    print(words_num) 

def avoids(word, unusable):
    for letter in word:
        if letter in unusable:
            return False
    return True

def uses_only(word, usable):
    for letter in word:
        if letter not in usable:
            return False
    return True

def uses_all(word, to_use):
    for letter in to_use:
        if letter not in word:
            return False
    return True

def uses_all1(word, to_use):
    return uses_only(to_use, word)

def has_3consecutive_double_letters(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def has_2consecutive_double_letters(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 2:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def authentication(f, word):
    if f(word):
        return 'Sei autenticato'
    return 'Password errata!'

def is_palindronic_odometer(number):
    if len(number) != 6:
        return
    i = 2
    j = 5
    count = 0
    while count <= 3:
        if number[i] != number[j] or number[i+1] != number[j-1]:
            return False
        count = count + 1
        number = str(int(number) + 1)
        if count == 1:
            i = i - 1
        if count == 2:
            j = j - 1
        if count == 3:
            i = i - 1
            j = j + 1
            if number [i+2] != number [j-2]:
                return False
    return True

def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.
    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s
 
def check(i):
    """Checks if the integer (i) has the desired properties.
    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))

def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1

# print('The following are the possible odometer readings:')
# check_all()
