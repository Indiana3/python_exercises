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

has_no_e()