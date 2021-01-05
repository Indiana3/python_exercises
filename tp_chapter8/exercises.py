"""
Verifica se una parola è palindroma

"""

def is_palindrome2(word):
    return word[::-1]

"""
Verifica se almeno un carattere della stringa è minuscolo

"""

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

"""
Verfica solo se il carattere 'c' è maiuscolo o minuscolo

"""

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

"""
Verifica se l'ultimo carattere è maiuscolo o minuscolo

"""

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

"""
Verifica se almeno un carattere della stringa è minuscolo,
ma con un flusso overcomplicato

"""

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

"""
Verfifica se tutti i caratteri di una stringa sono minuscoli

"""

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# print(is_palindrome2('aquila'))

# print(any_lowercase5('ciao'))

def rotate_word(s, n):
    for c in s:
        numeric_code_rotated = ord(c) + n
        chr_rotated = chr(numeric_code_rotated)
        print(chr_rotated, end="")

# rotate_word('squalo tigre', -1)

fin = open('C:/Users/Lorenzo/Desktop/Informatica/tomorrowDevs/learn_python/python_exercises/tp_chapter8/words.txt')
for line in fin:
    print(line.strip())
    
