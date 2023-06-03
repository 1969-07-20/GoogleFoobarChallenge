'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://jasonqsy.github.io/algorithm/2018/01/06/Google-foobar.html"


def answer(start, length):
    checksum = 0
    cur = start
    cur_len = length
    while cur_len > 0:
        checksum ^= xorsum(cur) ^ xorsum(cur + cur_len)
        cur += length
        cur_len -= 1

    return checksum

def xorsum(n):
    """
    Return 0^1^2^....^(n-1)
    """
    if n == 0:
        return 0

    if (n-1) % 4 == 0:
        return n-1
    elif (n-1) % 4 == 1:
        return 1
    elif (n-1) % 4 == 2:
        return n
    else:
        return 0
