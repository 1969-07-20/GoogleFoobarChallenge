'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/lcsm29/goog-foobar/blob/main/level3/prepare_the_bunnies_escape/solution.py"


def count_step(m, w, h):
    m = [[i for i in l] for l in m]
    next_pos = [(0, 0)]
    while next_pos:
        x, y = next_pos.pop(0)
        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x_, y_ = x + i, y + j
            if 0 <= x_ < w and 0 <= y_ < h:
                if not m[y_][x_]:
                    m[y_][x_] = m[y][x] + 1
                    next_pos.append((x_, y_))
    step = m[-1][-1]
    return step + 1 if step else float('inf')


def solution(m):
    w, h = len(m[0]), len(m)
    shortest_possible = w + h - 1
    if count_step(m, w, h) == shortest_possible:
        return shortest_possible
    shortest = float('inf')
    for x, y in [(x, y) for x in range(w) for y in range(h) if m[y][x]]:
        tmp = [[i for i in l] for l in m]
        tmp[y][x] = 0
        result = count_step(tmp, w, h)
        shortest = min(shortest, result)
        if result == shortest_possible:
            break
    return shortest
