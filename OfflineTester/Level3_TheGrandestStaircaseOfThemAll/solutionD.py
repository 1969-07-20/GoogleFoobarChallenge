'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/lcsm29/goog-foobar/blob/main/level3/the_grandest_staircase_of_them_all/solution.py"


def solution(n):
    smap = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    smap[0][0] = 1
    for y in range(1, n + 1):
        for x in range(n + 1):
            smap[y][x] = smap[y - 1][x]
            if x >= y:
                smap[y][x] += smap[y - 1][x - y]
    return smap[n][n] - 1
