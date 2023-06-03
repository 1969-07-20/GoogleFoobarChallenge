'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://stackoverflow.com/questions/42475706/google-foobar-number-station-coded-messages (Gaurav Sachdeva)"


def solution(l,t):
    sum=0
    j=0
    for keyi,i in enumerate(l):
        sum = sum + i
        while(sum>t and j < keyi ):
            sum = sum - l[j]
            j = j + 1
        if sum == t:
            return [j,keyi]

    return [-1,-1]
