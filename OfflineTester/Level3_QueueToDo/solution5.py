'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Raamkishore/Google-foobar-queue-to-do-Level-3/blob/master/queue_to_do.py"


def xor(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0

def solution(start, length):

    res = 0
    st = start - 1
    
    for i in range(length):
        sp = st + length - i
        res ^= xor(st) ^ xor(sp)
        st = sp + i

    return res

