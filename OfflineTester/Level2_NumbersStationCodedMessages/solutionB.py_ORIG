'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/smaranjitghose/Foobar_Challenge/blob/master/Solutions_Python/number_station_coded_messages.py"


def solution(l, t):
    length = len(l)
    for start_index in range(length):
        for end_index in range(start_index, length):
            goal = sum(l[start_index:end_index+1])
            if (goal > t):
                break
            if (goal == t):
                return [start_index, end_index]
    return [-1, -1]
