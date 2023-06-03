'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/atreids/foobar-minions/blob/master/solution.py"


def solution(data, n):
    newlist = data
    if len(data) > max(data):
        length = len(data)
    else:
        length = max(data)
    for i in range(length+1):
        if data.count(i) > n:
            for x in range(data.count(i)):
                newlist.remove(i)
    return newlist
