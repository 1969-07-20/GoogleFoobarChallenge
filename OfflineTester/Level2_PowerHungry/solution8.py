'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/lcsm29/goog-foobar/blob/main/level2/power_hungry/solution.py"


def solution(xs):
    if len(xs) <= 1:
        return str(xs[0]) if len(xs) else '0'
    xs = [n for n in xs if n]
    pos, neg = [n for n in xs if n > 0], [n for n in xs if n < 0]
    if len(neg) == len(pos + neg) == 1:
        return '0'
    if len(neg) % 2 == 1:
        neg.remove(max(neg))
    prod = 1
    for n in pos + neg:
        prod *= n
    return str(prod)
