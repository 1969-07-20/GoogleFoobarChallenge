'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Njeri-Marg/GoogleFooBarChallenge/blob/main/level2solution.py"


def solution(s):
    removed_dash=s.replace("-","")
    salutes=0
    for i,direction in enumerate(removed_dash):
        if direction == '>':
            front_soldiers=removed_dash[i:]
            left_soldiers=front_soldiers.count('<')
            salutes += left_soldiers *2
    return salutes
