'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://blog.finxter.com/googles-foobar"


def solution(n):
    x = int(n)
    c = 0

    while x > 1:
        if x & 1 == 1:
            # x is odd
            if x % 4 == 1 or x == 3:
                x -= 1
            else:
                x += 1
        else:
            # x is even
            x = x >> 1
        c += 1
    return c
