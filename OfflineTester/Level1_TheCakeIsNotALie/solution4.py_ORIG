from __future__ import division
from __future__ import print_function

'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://packetlost.com/blog/tag/the-cake-is-not-a-lie"


def answer(s):
    if not bool(s):
        return 0
    result = 0
    howlong = len(s)
    i = howlong
    while i > 0:
        n = howlong / i
        if (n * i) == howlong:
            valid = 1
            part = s[:int(n)]
            j = 1
            while j < i:
                if not s[int(j*n):int(j*n+n)] == part:
                    valid = 0
                    break
                j = j + 1
        if bool(valid):
            result = i
            break
        i = i - 1
    return result
