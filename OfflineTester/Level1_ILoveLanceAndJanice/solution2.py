'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://rajat19.github.io/foobar/i-love-lance-janice"


def solution(x):
    l = len(x)
    final = []
    for i in range(l):
        c = x[i]
        if 'a' <= c <= 'z':
            pos = ord(c) - ord('a')
            final.append(chr(ord('a') + 25 - pos))
        else:
            final.append(c)
    return ''.join(final)
