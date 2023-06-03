'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/timlines/minion-work-assignments/blob/main/minion-work-assignments"


def solution(data, n): 
    tempdata = []

    # Uses a for loop
    for i in data:
         # count each task
         x = data.count(i)
         if x <= n:
             # appends numbers to a new list
             tempdata.append(i)
    return tempdata
