'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://blog.finxter.com/googles-foobar"


def solution(l, t):
    
    start = stop = 0
    
    while start <= stop and stop < len(l):
        s = sum(l[start:stop+1])
        if s == t:
            return [start, stop]
        elif s < t:
            stop += 1
        else:
            start += 1
            stop = max(start, stop)
    
    return [-1, -1]
