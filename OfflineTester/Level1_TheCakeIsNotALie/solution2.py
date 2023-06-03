'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html"


def solution(s):
    if len(s) < 1: return 0
    if len(s) == 1: return 1

    p1 = 0
    p2 = 1
    orig = 1

    while p2 < len(s):
        while s[p1] != s[p2]:
            p2 += 1
            if p2 >= len(s):
                return 1

        if len(s)%p2 == 0:
            orig = p2
            while p2 < len(s) and s[p1] == s[p2]:
                p1 += 1
                p2 += 1
            if p2 >= len(s):
                return int(len(s)/orig)

        p1 = 0
        p2 += 1

    return 1
