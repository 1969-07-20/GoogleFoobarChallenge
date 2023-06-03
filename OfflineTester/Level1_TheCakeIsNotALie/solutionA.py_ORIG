'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/cmattoon/foobar/blob/master/the-cake-is-not-a-lie/solution.py"


def answer(s):
    L = len(s)
    for i in range(L):
        sub = s[:i]
        l = len(sub)
        occurs = s.count(sub)
        if occurs * l == L:
            return occurs
    return 1
