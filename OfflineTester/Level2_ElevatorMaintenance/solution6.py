'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Gargooie/Google_elevator_maintenance/blob/master/final.py"


def solution(l):
    array = sorted(l, key=lambda l:[int(y) for y in l.split('.')])
    return array
