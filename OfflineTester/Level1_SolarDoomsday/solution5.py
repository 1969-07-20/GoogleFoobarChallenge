'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://dev.to/itepsilon/foobar-solar-doomsday-5268"


from math import sqrt

def solution(area):
    res = []
    while area > 0:
        square = int(sqrt(area))**2
        area -= square
        res.append(square)
    return res
