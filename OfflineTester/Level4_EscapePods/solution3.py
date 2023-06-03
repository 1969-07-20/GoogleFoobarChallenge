'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/56865865/foobar-escape-pods-question-my-code-is-not-passing-all-tests (Shikhir Aggarwal)"


def solution(entrances, exits, path):
    le = len(entrances)
    lp = len(path)
    lx = len(exits)
    bunn_count = 0
    inter_paths = path[le:(lp-lx)]                # To find all intermediate rooms
    for i in range(lp - le - lx):                 # Loop through range of length of intermediate rooms
        sum_range = sum(inter_paths[i])           # Sum of an intermediate room's possible number of bunnies allowed
        sum_enter = 0                             # Sum of bunnies that enter that room
        for j in entrances:
            sum_enter += path[j][le + i]          # Get all bunnies that enter a room
        bunn_count += min(sum_enter, sum_range)
    return bunn_count
