'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/pijel/assorted-algos/blob/master/bomb_baby.py"


def answer(M, F):
    m = int(M)
    f = int(F)
    
    gen = 0
   
    while m>1 and f>1:
        if m>f:
            gen += m//f
            m = m % f
        if f>m:
            gen += f//m
            f = f%m
           
    if m == 1:
        return str(gen + f - 1)
    if f == 1:
        return str(gen + m - 1)
    return "impossible"
