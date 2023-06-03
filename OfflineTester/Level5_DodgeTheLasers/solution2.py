'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.oasys.net/posts/google-foobar-programming-challenge"


# Mod:
# - Cast return value of 's()' to int.


from decimal import *


def S(a, n):
    if n == 0:
        return 0
    np = int((a - 1) * n)
    return int(n * np + n * (n + 1) / 2 - np * (np + 1) / 2 - S(a, np))


def solution(s):
    getcontext().prec = 101
    return str(S(Decimal(2).sqrt(), int(s)))
