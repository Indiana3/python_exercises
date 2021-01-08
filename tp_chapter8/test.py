import os


def over_20_chr():
    fin = open("C:/Users/Lorenzo/Desktop/Informatica/tomorrowDevs/learn_python/python_exercises/tp_chapter8/words.txt")
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

def has_no_e():  
    fin = open(os.path.abspath('words.txt'))
    for line in fin:
        word = line.strip()
        for c in word:
            if c == 'e':
                print(word)

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

print(authentication(has_3consecutive_double_letters, 'aabbdcc'))

 




