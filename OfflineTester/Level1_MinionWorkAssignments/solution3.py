'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://hoangyell.com/fb1-google-foobar-minion-work-assignments"


from collections import Counter


def solution(data, n):
    counted_data = Counter(data)
    return [k for k in data if counted_data[k] <= n]
