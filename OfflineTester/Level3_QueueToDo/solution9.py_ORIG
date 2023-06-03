'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/45335975/trying-to-complete-google-foo-bar-level-3-queue-to-do-and-keep-exceeding-time (Josh Carvin)"


def answer(start, length):
    f = 0
    r = 0
    while f < length:
        for i in range(start, (start+length) - f):
            r ^= i
        f += 1
        start = range(start, start+length)[-1] + 1
    return r
