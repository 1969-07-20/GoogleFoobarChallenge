'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/n3a9/google-foobar/blob/master/Level%204/running_with_bunnies/solution.py"


import itertools

def convert_to_path(perm):
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i - 1], perm[i]))
    return path

def answer(time, time_limit):
    rows = len(time)
    bunnies = rows - 2

    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if time[i][j] > time[i][k] + time[k][j]:
                    time[i][j] = time[i][k] + time[k][j]

    for r in range(rows):
        if time[r][r] < 0:
            return [i for i in range(bunnies)]

    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_time += time[start][end]
            if total_time <= time_limit:
                return sorted(list(i - 1 for i in perm))
    return None
