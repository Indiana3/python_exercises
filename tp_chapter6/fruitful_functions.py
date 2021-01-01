"""
Esercizi con le fruitful functions. Una fruitful functions restituisce un valore

"""
"""
Confronta due numeri e restituisce un valore 

def test(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

x = input('Inserisci un primo valore')
y = input ('Inserisci un secondo valore')
print(test(x, y))

"""

import math
"""
Calcola la distanza tra 2 punti

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result

distance(1, 2, 4, 6)

"""
"""
Calcola l'ipotenusa di un triangolo rettangolo

def hypotenuse(a, b, c):
    side1 = b - a 
    side2 = c - a
    dsquared = side1 ** 2 + side2 ** 2
    result = math.sqrt(dsquared)
    print(result)

hypotenuse(2, 7, 3)

"""

"""
Confronta se il secondo numero inseriro è compreso tra il primo e il terzo


def is_between(x, y, z):
    if x<=y and y<=z:
        return True
    else:
        return False

x = int(input('Inserisci il primo valore'))
y = int(input('Inserisci il secondo valore'))
z = int(input('Inserisci il terzo valore'))

if is_between(x, y, z):
    print(y,'is between', x,'and', z)

"""

"""
n fattoriale

"""

def factorial(n):
    if n == 0:
        print(1)
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(result)
        return result

factorial(3)




