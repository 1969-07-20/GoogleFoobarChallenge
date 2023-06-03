'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/povstenko/power-hungry/blob/main/solution.py"


from functools import reduce

def solution(xs):
    if len(xs) == 0:
        return str(0)
    elif len(xs) == 1:
        return str(xs[0])

    pos = [i for i in xs if i > 0]
    neg = [i for i in xs if i < 0]

    if len(neg) % 2 == 1:
        neg.remove(max(neg))

    if len(neg) == 0 and len(pos) == 0:
        return str(0)

    res = reduce((lambda x,y: x*y), pos + neg)
    
    return str(res)
