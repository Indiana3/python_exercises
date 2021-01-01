"""
Esercizi con il while loop

"""

"""
Calcolo radice quadrata di un numero

x = 4
a = 6

while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y

"""


numero_balli = int(input('Quanti balli vuoi fare?'))

"""
Contatore balli con condizione a inizio ciclo

while numero_balli > 0:
    print('Sta per cominciare il prossimo ballo')
    numero_balli = numero_balli - 1

print('Hai terminato la sessione di ballo')


Contatore balli con condizione all'interno del ciclo

"""

while True:
    print('Sta per iniziare il tuo prossimo ballo')
    numero_balli = numero_balli - 1
    if numero_balli == 0:
        break

print('Hai terminato la sessione di ballo')
