'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/deep-woods/2021-Oct-Foobar/blob/main/Problems/Level%201%20Minion%20Labor%20Shifts.py"


def solution(data, n):
    data_frequency = {}
    adjusted_roster = []

    for d in data:
        if d not in data_frequency:
            data_frequency[d] = 1
        else:
            data_frequency[d] += 1

    for d in data:
        if data_frequency[d] > n:
            continue
        else:
            adjusted_roster.append(d)

    return adjusted_roster
