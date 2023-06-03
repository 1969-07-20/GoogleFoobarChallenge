'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://codereview.stackexchange.com/questions/252595/google-foobar-level-1-minion-task-schedule (yfr)"


def answer(data, n):
    if len(data) > 99:
        exit('List contains more than 100 elements')

    count = dict()
    for i in data:
        count.setdefault(i, 0)
        count[i] += 1

    for k, v in count.items():
        if v > n:
            for i in range(v):
                data.remove(k)

    return data
