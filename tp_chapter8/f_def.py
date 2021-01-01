"""
Esercizio paragrafo 8.6/8.7 di ThinkPython
la funzione verifica se una lettera è presente all'interno
di una parola e in caso affermativo restituisce in output il numero

"""

def find(word, letter, start):
    print(letter, end=': ')
    count = 0
    while start < len(word):
        if word[start] == letter:
            count = count + 1
        start = start + 1
    if count == 0:
        print('la lettera non è tra i caratteri controllati')
    else:
        print(count)

"""
Esercizio paragrafo 8.3 di ThinkPython

"""

def join(prefixes, suffix): 
    for letter in prefixes:
        print(letter, end='')          
        if letter == 'O' or letter == 'Q':
            print('u' + suffix)
        else:
            print(suffix)

"""
Funzione che prende una stringa come argomento e stampa
le singole lettere dalla fine

"""

def walking_backwards(s):
    index = len(s) - 1
    while True:
        letter = s[index]
        print(letter) 
        if index == 0:
            break
        index = index - 1

"""
Esercizio paragrafo 8.4 di ThinkPython

"""

fruit = 'banana'
fruit[:]

