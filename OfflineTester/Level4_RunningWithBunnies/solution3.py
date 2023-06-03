'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/lcsm29/goog-foobar/blob/main/level4/running_with_bunnies/solution.py"


from itertools import permutations


def solution(times, time_limit):
    time = [list(t) for t in times[:]]
    paths = lambda x: [(x[i - 1], x[i]) for i in range(1, len(x))]
    w = len(time)
    for k in range(w):
        for i in range(w):
            for j in range(w):
                if time[i][j] > time[i][k] + time[k][j]:
                    time[i][j] = time[i][k] + time[k][j]
    if any([1 for i in range(w) if time[i][i] < 0]):
        return [i for i in range(w - 2)]
    for i in range(w - 2, -1, -1):
        for p in permutations(range(1, w - 1), i):
            t = 0
            for s, e in paths([0] + list(p) + [-1]):
                t += time[s][e]
            if t <= time_limit:
                return sorted([i - 1 for i in p])
