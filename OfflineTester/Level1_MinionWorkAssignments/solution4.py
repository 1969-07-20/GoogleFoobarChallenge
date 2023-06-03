'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/lcsm29/goog-foobar/blob/main/level1/minion_work_assignments/solution.py"


def solution(data, n):  # the one that I submitted on Invitation #A3
    freq = {num: data.count(num) for num in data}
    return [num for num in data if freq[num] <= n]
