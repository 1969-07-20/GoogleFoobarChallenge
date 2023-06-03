'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/lcsm29/goog-foobar/blob/main/level3/bomb_baby/solution.py"


def solution(M, F):
    bombs = [int(M), int(F)]
    g = 0
    while bombs[0] - bombs[1]:
        bombs.sort()
        diff = bombs[1] - bombs[0]
        q, r = divmod(diff, bombs[0])
        g += q + (r > 0)
        bombs[1] -= (q + (r > 0)) * bombs[0]
    return str(g) if bombs == [1, 1] else 'impossible'

'''removed due to slow speed
def solution_brute(M, F):
    bombs = [int(M), int(F)]
    g = 0
    while bombs[0] - bombs[1]:
        bombs.sort()
        bombs[1] = bombs[1] - bombs[0]
        g += 1
    return str(g) if bombs == [1, 1] else 'impossible'
'''
