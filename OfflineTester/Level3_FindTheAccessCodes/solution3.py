'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html"


def solution(l):
    trips = 0
    doubs = [0]*len(l)

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                doubs[i] += 1
                trips += doubs[j]
    return trips
