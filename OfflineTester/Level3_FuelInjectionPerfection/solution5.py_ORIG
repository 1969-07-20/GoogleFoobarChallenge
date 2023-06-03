'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://www.oasys.net/posts/google-foobar-programming-challenge"


def solution(n):
    # count min number of add/subtract/halve operations to reach 1
    n = int(n)
    count = 0
    while n != 1:
        if n % 2:  # odd
            if n % 4 == 1 or n == 3:
                n -= 1  # subtract is better
            else:
                n += 1  # otherwise add
        else:  # even, halve
            n /= 2
        count += 1
    return count
