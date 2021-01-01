""" 
Esercizi con if e else

def even(x):
    if x%2 == 0:
        print( x, "is even")
    else:
        print( x, "is odd")
# even(5)

def do_n(f, x, n):
    if n<=0:
        return
    else:
        f(x)
        do_n(f, x, n-1)

do_n(even, 9, 4)

"""
"""
Esercizi con il while loop
def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

print_n('grogu', 6)
"""


    