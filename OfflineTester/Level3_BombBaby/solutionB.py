'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/ggarredondo/foo.bar-bomb-baby/blob/main/solution.py"


def solution(M, F):
    generations = -1
    iM = int(M)
    iF = int(F)

    while iM > 0 and iF > 0:
        if iM > iF:
            division = iM // iF
            iM %= iF
        else:
            division = iF // iM
            iF %= iM
        generations += division
    invalid = (iM == 0 and iF > 1) or (iM > 1 and iF == 0)

    result = str(generations)
    if invalid:
        result = "impossible"
    return result
